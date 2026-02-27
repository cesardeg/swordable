import { t } from './i18n.js';

const modalsHTML = `
<!-- Status Modal -->
<div class="modal-overlay" id="status-modal">
  <div class="modal">
    <div class="modal-titlebar">
      <div class="traffic"><div class="dot dot-red btn-close-modal" style="cursor:pointer"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
      <span style="font-family:'Share Tech Mono';font-size:11px;color:var(--text-dim);letter-spacing:.12em;margin-left:6px;" data-i18n="modal.status">STATUS</span>
    </div>
    <div class="modal-body">
      <div class="checkmark">✔</div>
      <div class="modal-message" id="status-message">—</div>
    </div>
    <div class="modal-footer">
      <button class="btn-modal btn-close-modal" data-i18n="modal.btn_ok">OK</button>
    </div>
  </div>
</div>

<!-- Manual Modal -->
<div class="modal-overlay" id="manual-modal">
  <div class="modal manual-modal">
    <div class="modal-titlebar">
      <div class="traffic"><div class="dot dot-red btn-close-modal" style="cursor:pointer"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
      <span style="font-family:'Cinzel',serif;font-size:11px;color:var(--text-main);letter-spacing:.18em;margin-left:6px;font-weight:600;" data-i18n="manual.title">Manual</span>
    </div>
    <div class="manual-body">
      <div class="manual-steps">
        <div class="manual-step"><span class="step-num">01</span><div class="step-content"><span class="step-title" data-i18n="manual.step1.title"></span><span class="step-desc" data-i18n="manual.step1.desc"></span></div></div>
        <div class="manual-step"><span class="step-num">02</span><div class="step-content"><span class="step-title" data-i18n="manual.step2.title"></span><span class="step-desc" data-i18n="manual.step2.desc"></span></div></div>
        <div class="manual-step"><span class="step-num">03</span><div class="step-content"><span class="step-title" data-i18n="manual.step3.title"></span><span class="step-desc" data-i18n="manual.step3.desc"></span></div></div>
        <div class="manual-step"><span class="step-num">04</span><div class="step-content"><span class="step-title" data-i18n="manual.step4.title"></span><span class="step-desc" data-i18n="manual.step4.desc"></span></div></div>
        <div class="manual-step"><span class="step-num">05</span><div class="step-content"><span class="step-title" data-i18n="manual.step5.title"></span><span class="step-desc" data-i18n="manual.step5.desc"></span></div></div>
      </div>
    </div>
    <div class="modal-footer" style="padding-top:0"><button class="btn-modal btn-close-modal" data-i18n="modal.btn_understood">OK</button></div>
  </div>
</div>

<!-- Error Modal -->
<div class="modal-overlay" id="error-modal">
  <div class="modal error-modal" id="error-modal-box">
    <div class="modal-titlebar">
      <div class="traffic"><div class="dot dot-red btn-close-modal" style="cursor:pointer"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
      <span style="font-family:'Share Tech Mono';font-size:11px;color:#c0392b;letter-spacing:.12em;margin-left:6px;" data-i18n="modal.error">ERROR</span>
    </div>
    <div class="error-body">
      <div class="error-icon">✖</div>
      <div class="error-content">
        <span class="error-title" id="error-title">Title</span>
        <span class="error-message" id="error-message">Message</span>
        <span class="error-detail" id="error-detail"></span>
      </div>
    </div>
    <div class="modal-footer" style="padding-top:0; padding-bottom:20px;"><button class="btn-error btn-close-modal" data-i18n="modal.btn_ok">OK</button></div>
  </div>
</div>
`;

export function initModals() {
    document.getElementById('modals-container').innerHTML = modalsHTML;

    const hideAll = () => document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('visible'));

    document.querySelectorAll('.btn-close-modal').forEach(btn => {
        btn.addEventListener('click', hideAll);
    });

    document.querySelectorAll('.modal-overlay').forEach(overlay => {
        overlay.addEventListener('click', (e) => {
            // Only close if clicking exactly on the overlay background, not the modal itself
            if (e.target === overlay) hideAll();
        });
    });
}

export function showStatus(message) {
    document.getElementById('status-message').innerHTML = message;
    document.getElementById('status-modal').classList.add('visible');
}

export function showManual() {
    document.getElementById('manual-modal').classList.add('visible');
}

export function showError(title, message, detail = '') {
    document.getElementById('error-title').innerHTML = title;
    document.getElementById('error-message').innerHTML = message;
    document.getElementById('error-detail').innerHTML = detail;

    const overlay = document.getElementById('error-modal');
    const box = document.getElementById('error-modal-box');
    overlay.classList.add('visible');

    // Trigger shake animation
    box.classList.remove('animate');
    void box.offsetWidth;
    box.classList.add('animate');
}
