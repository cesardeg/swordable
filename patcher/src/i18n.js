import pt from './locales/pt.json';
import es from './locales/es.json';

const locales = { pt, es };
// We default to pt, but allow build-time overrides via Vite
const currentLocale = import.meta.env.VITE_APP_LOCALE || 'pt';

export function t(key) {
    return locales[currentLocale][key] || key;
}

export function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        el.innerHTML = t(key);
    });

    // Replace document title
    document.title = t('app.title');
}
