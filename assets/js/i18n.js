/**
 * Simple I18n library for the portfolio
 */
const I18n = {
    currentLang: (function () {
        const htmlLang = (document.documentElement.lang || '').toLowerCase();
        if (htmlLang === 'en') return 'en';
        if (htmlLang === 'zh-cn') return 'zh-cn';
        if (htmlLang === 'zh-hk' || htmlLang === 'zh-tw') return 'zh-hk';
        try {
            return localStorage.getItem('lang') || 'en';
        } catch (error) {
            return 'en';
        }
    })(),
    data: {},

    async init() {
        await this.load(this.currentLang);
        this.apply();
        this.updateSwitcher();
    },

    async load(lang) {
        try {
            // Use absolute path to avoid issues with subdirectory deployments (e.g. Cloudflare Pages)
            const response = await fetch(`/assets/i18n/${lang}.json`);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status} while loading /assets/i18n/${lang}.json`);
            }
            this.data = await response.json();
            this.currentLang = lang;
            try {
                localStorage.setItem('lang', lang);
            } catch (storageError) {
                console.warn('Failed to persist selected language:', storageError);
            }
            document.documentElement.lang = lang === 'en' ? 'en' : (lang === 'zh-cn' ? 'zh-CN' : 'zh-HK');
        } catch (error) {
            console.error('Failed to load language file:', error);
            // Fallback: hide preloader even if i18n fails, so the page is not stuck
            document.getElementById('preloader') && (document.getElementById('preloader').style.display = 'none');
        }
    },

    apply() {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translation = this.getNestedValue(this.data, key);
            if (translation) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    if (el.placeholder) el.placeholder = translation;
                } else {
                    el.innerHTML = translation;
                }
            }
        });
        
        // Update titles if any
        const titleElements = document.querySelectorAll('[data-i18n-title]');
        titleElements.forEach(el => {
            const key = el.getAttribute('data-i18n-title');
            const translation = this.getNestedValue(this.data, key);
            if (translation) el.title = translation;
        });
    },

    getNestedValue(obj, key) {
        return key.split('.').reduce((o, i) => (o ? o[i] : null), obj);
    },

    async setLanguage(lang) {
        if (lang === this.currentLang) return;
        await this.load(lang);
        this.apply();
        this.updateSwitcher();
        // Dispatch event for any other listeners
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: lang }));
    },

    updateSwitcher() {
        // This can be used to update any UI elements that depend on the current language
        // but are not handled by data-i18n (e.g., active class on language buttons)
    }
};

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    I18n.init();
});
