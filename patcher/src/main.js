import { invoke } from '@tauri-apps/api/core';
import { getCurrentWindow } from '@tauri-apps/api/window';
import { open } from '@tauri-apps/plugin-dialog';

import { applyTranslations, t } from './i18n.js';
import { initModals, showStatus, showError, showManual } from './modals.js';

document.addEventListener('DOMContentLoaded', async () => {
  initModals();
  applyTranslations();

  // Window Controls - Native OS title bar is enabled
  const appWindow = getCurrentWindow();

  document.getElementById('btn-help').addEventListener('click', showManual);

  const pathInput = document.getElementById('path-input');
  const fieldRow = pathInput.closest('.field-row');
  const actionButtons = document.getElementById('action-buttons');
  const btnInstall = document.getElementById('btn-install');
  const btnReinstall = document.getElementById('btn-reinstall');
  const btnRemove = document.getElementById('btn-remove');

  // Scroll to end of path on focus and blur
  pathInput.addEventListener('focus', () => {
    setTimeout(() => {
      pathInput.select();
      pathInput.scrollLeft = pathInput.scrollWidth;
    }, 0);
  });

  pathInput.addEventListener('blur', () => {
    pathInput.scrollLeft = pathInput.scrollWidth;
  });

  function setPathInputValue(val) {
    pathInput.value = val;
    pathInput.scrollLeft = pathInput.scrollWidth;
    pathInput.setSelectionRange(val.length, val.length);
  }

  async function updateStatusButtons(path) {
    actionButtons.style.display = 'flex';
    if (!path) {
      fieldRow.classList.remove('error');
      btnInstall.textContent = t('patcher.not_found');
      btnInstall.disabled = true;
      btnInstall.style.opacity = '0.5';
      btnInstall.style.cursor = 'not-allowed';
      btnInstall.style.display = 'block';
      btnReinstall.style.display = 'none';
      btnRemove.style.display = 'none';
      return;
    }
    try {
      const isInstalled = await invoke('check_patch_status', { path });
      fieldRow.classList.remove('error');
      btnInstall.disabled = false;
      btnInstall.style.opacity = '1';
      btnInstall.style.cursor = 'pointer';

      if (isInstalled) {
        btnInstall.style.display = 'none';
        btnReinstall.style.display = 'block';
        btnRemove.style.display = 'block';
      } else {
        btnInstall.textContent = t('patcher.install');
        btnInstall.style.display = 'block';
        btnReinstall.style.display = 'none';
        btnRemove.style.display = 'none';
      }
    } catch (e) {
      console.warn("Folder validation failed:", e);
      fieldRow.classList.add('error');
      btnInstall.textContent = t('patcher.not_found');
      btnInstall.disabled = true;
      btnInstall.style.opacity = '0.5';
      btnInstall.style.cursor = 'not-allowed';
      btnInstall.style.display = 'block';
      btnReinstall.style.display = 'none';
      btnRemove.style.display = 'none';
    }
  }

  pathInput.addEventListener('input', (e) => {
    updateStatusButtons(e.target.value);
  });

  // Poll for external changes (e.g. from another instance or file explorer)
  setInterval(() => {
    if (pathInput.value) {
      updateStatusButtons(pathInput.value);
    }
  }, 2000);

  // Load initial path from rust
  try {
    const detected = await invoke('detect_path');
    if (detected) {
      setPathInputValue(detected);
      await updateStatusButtons(detected);
    } else {
      pathInput.placeholder = t('patcher.placeholder');
      await updateStatusButtons('');
    }
  } catch (e) {
    console.warn("No path detected.", e);
    pathInput.placeholder = t('patcher.placeholder');
    await updateStatusButtons('');
  }

  document.getElementById('btn-browse').addEventListener('click', async () => {
    try {
      const currentPath = pathInput.value && pathInput.value !== '...' ? pathInput.value : undefined;
      const selected = await open({
        directory: true,
        defaultPath: currentPath
      });
      if (selected) {
        pathInput.value = selected;
        await updateStatusButtons(selected);
      }
    } catch (e) {
      console.error(e);
    }
  });

  async function performInstall() {
    if (!pathInput.value) return;
    try {
      await invoke('install_patch', { path: pathInput.value });
      showStatus(t('patcher.install_success'));
      await updateStatusButtons(pathInput.value);
    } catch (e) {
      showError("Ocurrio un error", e);
    }
  }

  btnInstall.addEventListener('click', performInstall);
  btnReinstall.addEventListener('click', performInstall);

  btnRemove.addEventListener('click', async () => {
    if (!pathInput.value) return;
    try {
      await invoke('remove_patch', { path: pathInput.value });
      showStatus(t('patcher.remove_success'));
      await updateStatusButtons(pathInput.value);
    } catch (e) {
      showError(t('error.remove_failed.title'), t('error.remove_failed.msg'), e);
    }
  });
});
