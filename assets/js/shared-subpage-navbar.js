(function () {
  var container = document.getElementById('shared-subpage-navbar');
  if (!container) return;

  var htmlLang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
  var lang = 'en';
  if (htmlLang.indexOf('zh-cn') === 0) lang = 'zh-cn';
  else if (htmlLang.indexOf('zh-hk') === 0 || htmlLang.indexOf('zh-tw') === 0) lang = 'zh-hk';

  var section = (container.getAttribute('data-section') || '').toLowerCase();
  var copy = {
    en: {
      home: 'Home',
      welcome: 'Welcome',
      about: 'About',
      services: 'Service Offerings',
      contact: 'Contact',
      darkMode: 'Dark Mode',
      lightMode: 'Light Mode',
      capabilities: 'Capabilities',
      cases: 'Marketing',
      portfolio: 'Tech',
      investment: 'Investment',
      blog: 'Blog',
      blogArticles: 'Blog & Articles',
      language: 'Language',
      sites: 'Sites',
      homeHref: '/en/index.html',
      capabilitiesHref: '/en/capabilities.html',
      casesHref: '/en/mkt.html',
      portfolioHref: '/en/portfolio.html',
      investmentHref: '/en/invest.html',
      blogHref: '/en/blog/',
      web3: 'Web3 Research',
      web3Href: '/en/web3.html',
      web3Part1: 'Core & Logic',
      web3Part2: 'Regulation & Compliance',
      web3Part3: 'Business Value',
      web3Part4: 'Enterprise Entry',
      web3Part5: 'Trends & Challenges',
      web3Part6: 'Deep Dive Topics',
      web3Part7: 'Summary'
    },
    'zh-cn': {
      home: '\u9996\u9875',
      welcome: '\u6b22\u8fce',
      about: '\u5173\u4e8e\u6211',
      services: '\u670d\u52a1\u9879\u76ee',
      contact: '\u8054\u7cfb',
      darkMode: '\u6697\u8272\u6a21\u5f0f',
      lightMode: '\u4eae\u8272\u6a21\u5f0f',
      capabilities: '\u80fd\u529b',
      cases: '\u5e02\u573a\u5b66',
      portfolio: '\u6280\u672f',
      investment: '\u6295\u8d44',
      blog: '\u535a\u5ba2',
      blogArticles: '\u535a\u5ba2\u4e0e\u6587\u7ae0',
      language: '\u8bed\u8a00',
      sites: '\u7ad9\u70b9',
      homeHref: '/zh-cn/index.html',
      capabilitiesHref: '/zh-cn/capabilities.html',
      casesHref: '/zh-cn/mkt.html',
      portfolioHref: '/zh-cn/portfolio.html',
      investmentHref: '/zh-cn/invest.html',
      blogHref: '/zh-cn/blog/',
      web3: 'Web3\u4e13\u9898',
      web3Href: '/zh-cn/web3.html',
      web3Part1: '\u6838\u5fc3\u672c\u8d28\u4e0e\u5e95\u5c42\u903b\u8f91',
      web3Part2: '\u76d1\u7ba1\u4f53\u7cfb\u4e0e\u5408\u89c4',
      web3Part3: '\u5546\u4e1a\u4ef7\u503c\u4e0e\u6848\u4f8b',
      web3Part4: '\u4f01\u4e1a\u5165\u5c40\u8def\u5f84',
      web3Part5: '\u8d8b\u52bf\u4e0e\u6311\u6218',
      web3Part6: '\u4e94\u5927\u4e13\u9898\u7814\u7a76',
      web3Part7: '\u8ba4\u77e5\u6c47\u603b'
    },
    'zh-hk': {
      home: '\u9996\u9801',
      welcome: '\u6b61\u8fce',
      about: '\u95dc\u65bc\u6211',
      services: '\u670d\u52d9\u9805\u76ee',
      contact: '\u806f\u7d61',
      darkMode: '\u6df1\u8272\u6a21\u5f0f',
      lightMode: '\u4eae\u8272\u6a21\u5f0f',
      capabilities: '\u80fd\u529b',
      cases: '\u5e02\u5834\u5b78',
      portfolio: '\u6280\u8853',
      investment: '\u6295\u8cc7',
      blog: '\u535a\u5ba2',
      blogArticles: '\u535a\u5ba2\u8207\u6587\u7ae0',
      language: '\u8a9e\u8a00',
      sites: '\u7ad9\u9ede',
      homeHref: '/zh-hk/index.html',
      capabilitiesHref: '/zh-hk/capabilities.html',
      casesHref: '/zh-hk/mkt.html',
      portfolioHref: '/zh-hk/portfolio.html',
      investmentHref: '/zh-hk/invest.html',
      blogHref: '/zh-hk/blog/',
      web3: 'Web3\u5c08\u984c',
      web3Href: '/zh-hk/web3.html',
      web3Part1: '\u6838\u5fc3\u672c\u8cea\u8207\u5e95\u5c64\u908f\u8f2f',
      web3Part2: '\u76e3\u7ba1\u9ad4\u7cfb\u8207\u5408\u898f',
      web3Part3: '\u5546\u696d\u50f9\u503c\u8207\u6848\u4f8b',
      web3Part4: '\u4f01\u696d\u5165\u5c40\u8def\u5f91',
      web3Part5: '\u8da8\u52e2\u8207\u6311\u6230',
      web3Part6: '\u4e94\u5927\u5c08\u984c\u7814\u7a76',
      web3Part7: '\u8a8d\u77e5\u5f59\u7e3d'
    }
  };

  var labels = copy[lang];
  var altMap = {
    home: { en: copy.en.homeHref, zhCn: copy['zh-cn'].homeHref, zhHk: copy['zh-hk'].homeHref },
    capabilities: { en: copy.en.capabilitiesHref, zhCn: copy['zh-cn'].capabilitiesHref, zhHk: copy['zh-hk'].capabilitiesHref },
    cases: { en: copy.en.casesHref, zhCn: copy['zh-cn'].casesHref, zhHk: copy['zh-hk'].casesHref },
    portfolio: { en: copy.en.portfolioHref, zhCn: copy['zh-cn'].portfolioHref, zhHk: copy['zh-hk'].portfolioHref },
    investment: { en: copy.en.investmentHref, zhCn: copy['zh-cn'].investmentHref, zhHk: copy['zh-hk'].investmentHref },
    web3: { en: copy.en.web3Href, zhCn: copy['zh-cn'].web3Href, zhHk: copy['zh-hk'].web3Href },
    blog: { en: copy.en.blogHref, zhCn: copy['zh-cn'].blogHref, zhHk: copy['zh-hk'].blogHref },
  };
  var alt = altMap[section] || altMap.blog;
  function langUrl(t) { var els = document.querySelectorAll('#shared-subpage-navbar .hidden-trans'); var key = {en:'en',zhCn:'zh-cn',zhHk:'zh-hk'}[t]; for (var i=0;i<els.length;i++) { if (els[i].getAttribute('data-lang') === key) return els[i].getAttribute('data-url'); } var c = window.location.pathname; if (c === '/' || c === '/index.html') return alt[t]; var p = {en:'en',zhCn:'zh-cn',zhHk:'zh-hk'}; var x = '/' + lang + '/'; if (c.indexOf(x) === 0) return c.replace(x, '/' + p[t] + '/'); return alt[t]; }

  var siteLinks = [
    { label: 'GitHub', href: 'https://github.com/fengyuwang-com' },
    { label: 'LinkedIn', href: 'https://linkedin.com/in/fengyuwang-com/' },
    { label: 'YouTube', href: 'https://www.youtube.com/@fenglin6' },
    { label: 'BiliBili', href: 'https://b23.tv/Aqk6EGE' }
  ];
  var siteLinksHtml = siteLinks
    .map(function (link) {
      return '            <li><a href="' + link.href + '" target="_blank" rel="noopener noreferrer">' + link.label + '</a></li>';
    })
    .join('');

  var oldStyle = document.getElementById('shared-subpage-navbar-style');
  if (oldStyle) oldStyle.remove();
  var style = document.createElement('style');
    style.id = 'shared-subpage-navbar-style';
    style.textContent = [
      /* ---- Base ---- */
      '.shared-subpage-nav { position: fixed; top: 0; left: 0; right: 0; z-index: 9999; background: rgba(255, 255, 255, 0.72); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px); box-shadow: 0 1px 0 rgba(0,0,0,0.1); }',
      '.shared-subpage-nav .nav-shell { max-width: 1200px; margin: 0 auto; padding: 0 20px; min-height: 44px; display: flex; align-items: center; justify-content: space-between; gap: 20px; }',
      '.shared-subpage-nav .brand img { height: 32px; display: block; }',
      '.shared-subpage-nav .desktop-menu, .shared-subpage-nav .desktop-menu ul, .shared-subpage-nav .mobile-menu, .shared-subpage-nav .mobile-menu ul { list-style: none; margin: 0; padding: 0; }',
      '.shared-subpage-nav .desktop-menu { display: flex; align-items: center; gap: 2px; flex-wrap: wrap; }',
      '.shared-subpage-nav .desktop-menu > li, .shared-subpage-nav .mobile-menu > li { position: relative; }',
      '.shared-subpage-nav a { text-decoration: none; }',
      '.shared-subpage-nav .desktop-menu a, .shared-subpage-nav .mobile-link, .shared-subpage-nav .mobile-submenu a { display: block; padding: 8px 12px; color: #1d1d1f; font-size: 12px; font-weight: 400; }',
      '.shared-subpage-nav .desktop-menu a:hover, .shared-subpage-nav .desktop-menu a.active, .shared-subpage-nav .mobile-link:hover, .shared-subpage-nav .mobile-link.active, .shared-subpage-nav .mobile-submenu a:hover { color: #0071e3; }',

      /* ---- Desktop submenu: Apple-style fade + scale + glass ---- */
      '.shared-subpage-nav .desktop-menu .submenu { position: absolute; display: none; }',
      '/* submenu controlled by portal */',
      '.shared-subpage-nav .desktop-menu .submenu a { padding: 8px 18px; border-bottom: 1px solid rgba(0,0,0,.05); background: transparent; white-space: nowrap; transition: background 0.15s ease; }',
      '.shared-subpage-nav .desktop-menu .submenu li:last-child a { border-bottom: 0; }',
      '.shared-subpage-nav .desktop-menu .submenu a:hover { background: rgba(0,113,227,0.06); }',

      /* ---- Desktop submenu caret icon ---- */
      '.shared-subpage-nav .desktop-menu .nav-caret { display: inline-block; margin-left: 4px; font-size: 8px; transition: transform 0.2s ease; }',
      '.shared-subpage-nav .desktop-menu li:hover > a .nav-caret { transform: rotate(180deg); }',

      /* ---- Social / theme ---- */
      '.shared-subpage-nav .social { display: inline-flex; align-items: center; gap: 12px; }',
      '.shared-subpage-nav .theme-toggle { display: inline-flex; align-items: center; justify-content: center; gap: 6px; min-height: 32px; padding: 6px 12px; border: 0; border-radius: 20px; background: rgba(0,0,0,0.08); color: #1d1d1f; cursor: pointer; font-size: 12px; font-weight: 400; transition: background .2s ease; }',
      '.shared-subpage-nav .theme-toggle:hover { background: rgba(0,0,0,0.12); }',
      '.shared-subpage-nav .theme-toggle:active, .shared-subpage-nav .theme-toggle.is-pressed { background: rgba(0,0,0,0.16); }',
      '.shared-subpage-nav .theme-toggle .fa-sun { display: none; }',
      '.shared-subpage-nav .theme-toggle-text { line-height: 1; }',

      /* ---- Menu toggle (hamburger) ---- */
      '.shared-subpage-nav .menu-toggle { display: none; width: 36px; height: 36px; border: 0; border-radius: 8px; background: rgba(0,0,0,0.08); cursor: pointer; padding: 0; }',
      '.shared-subpage-nav .menu-toggle span { display: block; width: 16px; height: 1.5px; background: #0a0e1a; margin: 6px auto; transition: transform .2s ease, opacity .2s ease; }',

      /* ---- Mobile panel ---- */
      '.shared-subpage-nav .mobile-panel { display: none; border-top: 1px solid rgba(0,0,0,.06); padding: 8px 20px 24px; background: rgba(255,255,255,0.85); backdrop-filter: saturate(180%) blur(20px); }',
      '.shared-subpage-nav .mobile-panel.open { display: block; }',
      '.shared-subpage-nav .mobile-link-row { display: flex; align-items: center; justify-content: space-between; gap: 12px; cursor: pointer; }',
      '.shared-subpage-nav .mobile-link-row > span { display: block; padding: 8px 12px; color: #1d1d1f; font-size: 12px; font-weight: 400; }',
      '.shared-subpage-nav .mobile-item { }',
      '.shared-subpage-nav .mobile-submenu { max-height: 0; overflow: hidden; padding-left: 12px; transition: max-height 0.35s ease; }',
      '.shared-subpage-nav .mobile-item.open > .mobile-submenu { max-height: 500px; }',
      '.shared-subpage-nav .mobile-menu > li + li { border-top: 1px solid rgba(0,0,0,.06); }',
      '.shared-subpage-nav .mobile-social { padding: 12px 12px 20px; }',

      /* ---- Mobile panel portal (body-level backdrop-filter) ---- */
      '#mobile-panel-portal { position: fixed; top: 44px; left: 0; right: 0; z-index: 9998; background: rgba(255,255,255,0.85); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px); box-shadow: 0 18px 48px rgba(0,0,0,0.12); opacity: 0; pointer-events: none; transform: translateY(-10px); transition: opacity 0.3s ease, transform 0.3s ease; }',
      '#mobile-panel-portal.open { opacity: 1; pointer-events: auto; transform: translateY(0); }',
      '#mobile-panel-portal .shared-subpage-nav .mobile-panel { border-top: 1px solid rgba(0,0,0,.06); padding: 8px 20px 24px; }',
      '#mobile-panel-portal .mobile-link-row { display: flex; align-items: center; justify-content: space-between; gap: 12px; cursor: pointer; }',
      '#mobile-panel-portal .mobile-link-row > span { display: block; padding: 12px 12px; color: #1d1d1f; font-size: 18px; font-weight: 500; }',
      '#mobile-panel-portal .mobile-item { }',
      '#mobile-panel-portal .mobile-submenu { max-height: 0; overflow: hidden; padding-left: 12px; transition: max-height 0.35s ease; }',
      '#mobile-panel-portal .mobile-submenu a { font-size: 15px; font-weight: 400; }',
      '#mobile-panel-portal .mobile-item.open > .mobile-submenu { max-height: 500px; }',
      '#mobile-panel-portal .mobile-menu > li + li { border-top: 1px solid rgba(0,0,0,.06); }',
      '#mobile-panel-portal .mobile-menu a { display: block; padding: 12px 12px; color: #1d1d1f; font-size: 18px; font-weight: 500; text-decoration: none; }',
      '#mobile-panel-portal .mobile-menu a:hover { color: #0071e3; }',
      '#mobile-panel-portal .mobile-social { padding: 12px 12px 20px; }',
      '#mobile-panel-portal .theme-toggle { display: inline-flex; align-items: center; justify-content: center; gap: 6px; min-height: 32px; padding: 6px 12px; border: 0; border-radius: 20px; background: rgba(0,0,0,0.08); color: #1d1d1f; cursor: pointer; font-size: 12px; font-weight: 400; transition: background .2s ease; }',
      '#mobile-panel-portal .theme-toggle:hover { background: rgba(0,0,0,0.12); }',
      '#mobile-panel-portal .theme-toggle .fa-sun { display: none; }',

      /* ---- Body offset ---- */
      '#submenu-portal { position: fixed; z-index: 10000; pointer-events: none; }',
      '#submenu-portal.active { pointer-events: auto; }',
      '#submenu-portal .sp-wrap { margin-top: 8px; min-width: 200px; padding: 6px 0; background: rgba(255,255,255,0.72); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px); border-radius: 14px; border: 0.5px solid rgba(255,255,255,0.3); box-shadow: 0 18px 48px rgba(0,0,0,0.12), 0 0 0 0.5px rgba(255,255,255,0.04); opacity: 0; transform: translateY(-6px); transition: opacity 0.2s ease, transform 0.25s cubic-bezier(0.25,0.1,0.25,1); }',
      '#submenu-portal.active .sp-wrap { opacity: 1; transform: translateY(0); }',
      '#submenu-portal .sp-wrap a { display: block; padding: 8px 18px; border-bottom: 1px solid rgba(0,0,0,0.05); background: transparent; white-space: nowrap; color: #1d1d1f; font-size: 12px; font-weight: 400; text-decoration: none; }',
      '#submenu-portal .sp-wrap li:last-child a { border-bottom: 0; }',
      '#submenu-portal .sp-wrap a:hover { color: #0071e3; background: rgba(0,113,227,0.06); }',
      '#submenu-portal .sp-wrap ul { list-style: none; margin: 0; padding: 0; }',
      '#submenu-portal .sp-wrap li { list-style: none; }',
      'body[data-theme="dark"] #submenu-portal .sp-wrap { background: rgba(10, 14, 26, 0.72); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px); border: 0.5px solid rgba(255,255,255,0.06); box-shadow: 0 18px 48px rgba(0,0,0,0.4), 0 0 0 0.5px rgba(255,255,255,0.04); }',
      'body[data-theme="dark"] #submenu-portal .sp-wrap a { color: #f5f5f7; background: transparent; border-color: rgba(255,255,255,0.04); }',
      'body[data-theme="dark"] #submenu-portal .sp-wrap a:hover { color: #2997ff; background: rgba(41,151,255,0.08); }',
      'body { padding-top: 44px !important; }',

      /* ---- Dark mode ---- */
      'body[data-theme="dark"] { background: #0a0e1a !important; color: #f5f5f7; }',
      'body[data-theme="dark"] .shared-subpage-nav { background: rgba(10, 14, 26, 0.72); box-shadow: 0 1px 0 rgba(255,255,255,0.1); }',
      'body[data-theme="dark"] .shared-subpage-nav .desktop-menu a, body[data-theme="dark"] .shared-subpage-nav .mobile-link, body[data-theme="dark"] .shared-subpage-nav .mobile-submenu a { color: #f5f5f7; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-link-row > span { color: #f5f5f7; }',
      'body[data-theme="dark"] .shared-subpage-nav .desktop-menu a:hover, body[data-theme="dark"] .shared-subpage-nav .mobile-link:hover { color: #2997ff; }',
      'body[data-theme="dark"] .shared-subpage-nav .desktop-menu .submenu { display: none; }',
      'body[data-theme="dark"] .shared-subpage-nav .desktop-menu .submenu a { background: transparent; border-color: rgba(255,255,255,0.04); }',
      'body[data-theme="dark"] .shared-subpage-nav .desktop-menu .submenu a:hover { background: rgba(41,151,255,0.08); }',
      'body[data-theme="dark"] .shared-subpage-nav .theme-toggle { background: rgba(255,255,255,0.1); color: #f5f5f7; }',
      'body[data-theme="dark"] .shared-subpage-nav .theme-toggle:hover { background: rgba(255,255,255,0.15); }',
      'body[data-theme="dark"] .shared-subpage-nav .menu-toggle { background: rgba(255,255,255,0.1); }',
      'body[data-theme="dark"] .shared-subpage-nav .menu-toggle span { background: #f5f5f7; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-panel { background: rgba(10, 14, 26, 0.85); }',
      'body[data-theme="dark"] #mobile-panel-portal { background: rgba(10, 14, 26, 0.85); opacity: 0; pointer-events: none; transform: translateY(-10px); }',
      'body[data-theme="dark"] #mobile-panel-portal.open { opacity: 1; pointer-events: auto; transform: translateY(0); }',
      'body[data-theme="dark"] #mobile-panel-portal .mobile-menu a { color: #f5f5f7; }',
      'body[data-theme="dark"] #mobile-panel-portal .mobile-menu a:hover { color: #2997ff; }',
      'body[data-theme="dark"] #mobile-panel-portal .mobile-link-row > span { color: #f5f5f7; }',
      'body[data-theme="dark"] #mobile-panel-portal .theme-toggle { background: rgba(255,255,255,0.1); color: #f5f5f7; }',
      'body[data-theme="dark"] #mobile-panel-portal .theme-toggle:hover { background: rgba(255,255,255,0.15); }',
      'body[data-theme="dark"] #mobile-panel-portal .theme-toggle .fa-moon { display: none; }',
      'body[data-theme="dark"] #mobile-panel-portal .theme-toggle .fa-sun { display: inline-block; }',
      'body[data-theme="dark"] .theme-toggle .fa-moon { display: none; }',
      'body[data-theme="dark"] .theme-toggle .fa-sun { display: inline-block; }',
      'body[data-theme="dark"] .single-services-item, body[data-theme="dark"] .project-card, body[data-theme="dark"] .content-card, body[data-theme="dark"] .node-card, body[data-theme="dark"] .tree-shell { background: #1e293b !important; color: #e5ecf4 !important; border-color: rgba(148,163,184,.20) !important; }',
      'body[data-theme="dark"] .single-services-item h3, body[data-theme="dark"] .project-card h3, body[data-theme="dark"] .content-card h3 { color: #e5ecf4 !important; }',
      'body[data-theme="dark"] .single-services-item p, body[data-theme="dark"] .project-card p, body[data-theme="dark"] .content-card p { color: #9fb0c3 !important; }',
      'body[data-theme="dark"] .page-header h1, body[data-theme="dark"] .section-title h2 { color: #e5ecf4 !important; }',
      'body[data-theme="dark"] .page-header p, body[data-theme="dark"] .section-title p { color: #9fb0c3 !important; }',
      'body[data-theme="dark"] .bg-grey, body[data-theme="dark"] .services-section { background: #111827 !important; }',

      /* ---- Responsive ---- */
      '@media (max-width: 991px) { .shared-subpage-nav .nav-shell { min-height: 44px; } .shared-subpage-nav .nav-main { display: none; } .shared-subpage-nav .menu-toggle { display: inline-block; } }'
    ].join('');
    document.head.appendChild(style);

  var active = {
    home: section === 'home' ? ' active' : '',
    capabilities: section === 'capabilities' ? ' active' : '',
    cases: section === 'cases' ? ' active' : '',
    portfolio: section === 'portfolio' ? ' active' : '',
    investment: section === 'investment' ? ' active' : '',
    blog: section === 'blog' ? ' active' : '',
  };

  container.outerHTML = [
    '<div class="shared-subpage-nav">',
    '  <div class="nav-shell">',
    '    <a class="brand" href="' + labels.homeHref + '">',
    '      <img src="/assets/img/logo-black.png" alt="logo">',
    '    </a>',
    '    <div class="nav-main">',
    '      <ul class="desktop-menu">',
    '        <li>',
    '          <a href="' + labels.homeHref + '" class="' + active.home.trim() + '">' + labels.home + ' <i class="fas fa-chevron-down nav-caret"></i></a>',
    '          <ul class="submenu">',
    '            <li><a href="' + labels.homeHref + '#welcome">' + labels.welcome + '</a></li>',
    '            <li><a href="' + labels.homeHref + '#about">' + labels.about + '</a></li>',
    '            <li><a href="' + labels.homeHref + '#tracks">' + (lang === 'en' ? 'Explore the site by track' : lang === 'zh-cn' ? '\u6309\u4e3b\u7ebf\u6d4f\u89c8\u7f51\u7ad9' : '\u6309\u4e3b\u7dda\u700f\u89bd\u7db2\u7ad9') + '</a></li>',
    '          </ul>',
    '        </li>',
    '        <li><a href="' + labels.capabilitiesHref + '" class="' + active.capabilities.trim() + '">' + labels.capabilities + '</a></li>',
    '        <li><a href="' + labels.casesHref + '" class="' + active.cases.trim() + '">' + labels.cases + '</a></li>',
    '        <li>',
    '          <a href="' + labels.portfolioHref + '" class="' + active.portfolio.trim() + '">' + labels.portfolio + ' <i class="fas fa-chevron-down nav-caret"></i></a>',
    '          <ul class="submenu">',
    '            <li><a href="' + labels.portfolioHref + '">' + labels.portfolio + '</a></li>',
    '            <li><a href="' + labels.web3Href + '">' + labels.web3 + '</a></li>',
    '          </ul>',
    '        </li>',
    '        <li><a href="' + labels.investmentHref + '" class="' + active.investment.trim() + '">' + labels.investment + '</a></li>',
    '        <li><a href="' + labels.blogHref + '" class="' + active.blog.trim() + '">' + labels.blog + '</a></li>',
        '        <li>',
        '          <a href="#">' + labels.sites + ' <i class="fas fa-chevron-down nav-caret"></i></a>',
        '          <ul class="submenu">',
        siteLinksHtml,
        '          </ul>',
        '        </li>',
    '        <li>',
    '          <a href="#">' + labels.language + ' <i class="fas fa-chevron-down nav-caret"></i></a>',
    '          <ul class="submenu">',
    '            <li><a href="' + langUrl('en') + '">English</a></li>',
    '            <li><a href="' + langUrl('zhCn') + '">\u7b80\u4f53\u4e2d\u6587</a></li>',
    '            <li><a href="' + langUrl('zhHk') + '">\u7e41\u9ad4\u4e2d\u6587</a></li>',
    '          </ul>',
    '        </li>',
    '      </ul>',
    '    </div>',
    '    <div class="social nav-main"><button class="theme-toggle" type="button" aria-pressed="false"><i class="fas fa-moon"></i><i class="fas fa-sun"></i><span class="theme-toggle-text">' + labels.darkMode + '</span></button></div>',
    '    <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Toggle menu">',
    '      <span></span><span></span><span></span>',
    '    </button>',
    '  </div>',
    '  <div class="mobile-panel">',
    '    <ul class="mobile-menu">',
    '      <li class="mobile-item">',
    '        <div class="mobile-link-row" data-toggle-submenu>',
    '          <a class="mobile-link' + active.home + '" href="' + labels.homeHref + '" onclick="event.stopPropagation()">' + labels.home + '</a>',
    '          <span class="mobile-caret">&#x2039;</span>',
    '        </div>',
    '        <ul class="mobile-submenu">',
    '          <li><a href="' + labels.homeHref + '#welcome">' + labels.welcome + '</a></li>',
    '          <li><a href="' + labels.homeHref + '#about">' + labels.about + '</a></li>',
    '          <li><a href="' + labels.homeHref + '#tracks">' + (lang === 'en' ? 'Explore the site by track' : lang === 'zh-cn' ? '\u6309\u4e3b\u7ebf\u6d4f\u89c8\u7f51\u7ad9' : '\u6309\u4e3b\u7dda\u700f\u89bd\u7db2\u7ad9') + '</a></li>',
    '        </ul>',
    '      </li>',
    '      <li><a class="mobile-link' + active.capabilities + '" href="' + labels.capabilitiesHref + '">' + labels.capabilities + '</a></li>',
    '      <li><a class="mobile-link' + active.cases + '" href="' + labels.casesHref + '">' + labels.cases + '</a></li>',
    '      <li class="mobile-item">',
    '        <div class="mobile-link-row" data-toggle-submenu>',
    '          <a class="mobile-link' + active.portfolio + '" href="' + labels.portfolioHref + '" onclick="event.stopPropagation()">' + labels.portfolio + '</a>',
    '          <span class="mobile-caret">&#x2039;</span>',
    '        </div>',
    '        <ul class="mobile-submenu">',
    '          <li><a href="' + labels.portfolioHref + '">' + labels.portfolio + '</a></li>',
    '          <li><a href="' + labels.web3Href + '">' + labels.web3 + '</a></li>',
    '        </ul>',
    '      </li>',
    '      <li><a class="mobile-link' + active.blog + '" href="' + labels.blogHref + '">' + labels.blog + '</a></li>',
      '      <li class="mobile-item">',
      '        <div class="mobile-link-row" data-toggle-submenu>',
      '          <span>' + labels.sites + '</span>',
      '          <span class="mobile-caret">&#x2039;</span>',
      '        </div>',
      '        <ul class="mobile-submenu">',
      siteLinksHtml,
      '        </ul>',
      '      </li>',
    '      <li class="mobile-item">',
    '        <div class="mobile-link-row" data-toggle-submenu>',
    '          <span>' + labels.language + '</span>',
    '          <span class="mobile-caret">&#x2039;</span>',
    '        </div>',
    '        <ul class="mobile-submenu">',
    '          <li><a href="' + langUrl('en') + '">English</a></li>',
    '          <li><a href="' + langUrl('zhCn') + '">\u7b80\u4f53\u4e2d\u6587</a></li>',
    '          <li><a href="' + langUrl('zhHk') + '">\u7e41\u9ad4\u4e2d\u6587</a></li>',
    '        </ul>',
    '      </li>',
    '    </ul>',
    '    <div class="mobile-social"><button class="theme-toggle" type="button" aria-pressed="false"><i class="fas fa-moon"></i><i class="fas fa-sun"></i><span class="theme-toggle-text">' + labels.darkMode + '</span></button></div>',
    '  </div>',
    '</div>'
  ].join('');

  // ---- Inject mobile caret styles ----
  var oldCaretStyle = document.getElementById('shared-nav-caret-style');
  if (oldCaretStyle) oldCaretStyle.remove();
  var cs = document.createElement('style');
    cs.id = 'shared-nav-caret-style';
    cs.textContent = [
      '.shared-subpage-nav .mobile-caret { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; font-size: 18px; color: #6e6e73; transition: transform 0.2s ease; flex: 0 0 auto; }',
      '.shared-subpage-nav .mobile-item.open > .mobile-link-row .mobile-caret { transform: rotate(90deg); color: #0071e3; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-caret { color: #86868b; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-item.open > .mobile-link-row .mobile-caret { color: #2997ff; }'
    ].join('');
    document.head.appendChild(cs);

  function applyTheme(theme) {
    document.body.setAttribute('data-theme', theme);
    try { localStorage.setItem('site-theme', theme); } catch (e) {}
    var text = theme === 'dark' ? labels.darkMode : labels.lightMode;
    Array.prototype.forEach.call(document.querySelectorAll('.theme-toggle'), function (btn) {
      btn.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
      var span = btn.querySelector('.theme-toggle-text');
      if (span) span.textContent = text;
    });
  }
  function currentTheme() {
    return document.body.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }
  var saved = null;
  try { saved = localStorage.getItem('site-theme'); } catch (e) {}
  if (!saved) {
    saved = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  applyTheme(saved);

  var nav = document.querySelector('.shared-subpage-nav');
  if (!nav) return;


  // ---- Move mobile panel to body level for correct backdrop-filter ----
  var mobilePanel = nav.querySelector('.mobile-panel');
  var mobilePortal = document.getElementById('mobile-panel-portal');
  if (mobilePanel && !mobilePortal) {
    mobilePortal = document.createElement('div');
    mobilePortal.id = 'mobile-panel-portal';
    mobilePortal.className = 'open';
    mobilePortal.appendChild(mobilePanel);
    document.body.appendChild(mobilePortal);
    mobilePortal.classList.remove('open');
  }

  // ---- Hamburger toggle (now toggles body-level portal) ----
  var toggle = nav.querySelector('.menu-toggle');
  if (toggle && mobilePortal) {
    toggle.addEventListener('click', function () {
      var open = mobilePortal.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ---- Desktop: portal submenu (body-level backdrop-filter) ----
  var portal = document.getElementById('submenu-portal');
  if (!portal) {
    portal = document.createElement('div');
    portal.id = 'submenu-portal';
    document.body.appendChild(portal);
    var pw = document.createElement('div');
    pw.className = 'sp-wrap';
    portal.appendChild(pw);
  }
  var portalWrap = portal.querySelector('.sp-wrap');
  Array.prototype.forEach.call(nav.querySelectorAll('.desktop-menu > li'), function (li) {
    var sub = li.querySelector('.submenu');
    if (!sub) return;
    var t;
    function sp() {
      var r = li.getBoundingClientRect();
      portalWrap.innerHTML = sub.innerHTML;
      portal.style.top = (r.bottom + 4) + 'px';
      portal.style.left = (r.left + r.width / 2) + 'px';
      portal.style.transform = 'translateX(-50%)';
      portalWrap.style.opacity = '0';
      portalWrap.style.transform = 'translateY(-6px)';
      portal.classList.add('active');
      portalWrap.getBoundingClientRect();
      portalWrap.style.opacity = '1';
      portalWrap.style.transform = 'translateY(0)';
    }
    function hp() {
      portalWrap.style.opacity = '0';
      portalWrap.style.transform = 'translateY(-6px)';
      setTimeout(function(){portal.classList.remove('active')},200);
    }
    li.addEventListener('mouseenter',function(){clearTimeout(t);sp()});
    li.addEventListener('mouseleave',function(){t=setTimeout(hp,100)});
    portal.addEventListener('mouseenter',function(){clearTimeout(t)});
    portal.addEventListener('mouseleave',function(){t=setTimeout(hp,100)});
  });

  // ---- Mobile: click on row toggles submenu (query from body-level portal) ----
  function initMobileSubmenus(root) {
    Array.prototype.forEach.call(root.querySelectorAll('.mobile-item'), function (item) {
      var row = item.querySelector('.mobile-link-row');
      var link = row && row.querySelector('a');
      if (!row) return;
      row.addEventListener('click', function (e) {
        if (link && e.target && (e.target === link || link.contains(e.target))) return;
        var open = item.classList.toggle('open');
        if (open) {
          Array.prototype.forEach.call(root.querySelectorAll('.mobile-item.open'), function (other) {
            if (other !== item) other.classList.remove('open');
          });
        }
        Array.prototype.forEach.call(item.querySelectorAll('[data-expanded]'), function (el) {
          el.setAttribute('data-expanded', open ? 'true' : 'false');
        });
      });
    });
  }
  if (mobilePortal) initMobileSubmenus(mobilePortal);

  Array.prototype.forEach.call(nav.querySelectorAll('.theme-toggle'), function (btn) {
  // Also attach theme-toggle handlers for mobile portal toggles (moved to body)
  if (mobilePortal) {
    Array.prototype.forEach.call(mobilePortal.querySelectorAll('.theme-toggle'), function (btn) {
      btn.addEventListener('click', function () {
        applyTheme(currentTheme() === 'dark' ? 'light' : 'dark');
        btn.classList.add('is-pressed');
        window.setTimeout(function () { btn.classList.remove('is-pressed'); }, 160);
      });
    });
  }

  // ---- Close mobile menu on orientation change (portrait -> landscape) ----
  var mq = window.matchMedia('(min-width: 992px)');
  function handleMqChange(e) {
    if (e.matches && mobilePortal) {
      mobilePortal.classList.remove('open');
      var t = nav.querySelector('.menu-toggle');
      if (t) t.setAttribute('aria-expanded', 'false');
    }
  }
  mq.addEventListener('change', handleMqChange);
    btn.addEventListener('click', function () {
      applyTheme(currentTheme() === 'dark' ? 'light' : 'dark');
      btn.classList.add('is-pressed');
      window.setTimeout(function () { btn.classList.remove('is-pressed'); }, 160);
    });
  });
  window.__siteTheme = {
    applyTheme: applyTheme,
    toggleTheme: function () { applyTheme(currentTheme() === 'dark' ? 'light' : 'dark'); },
    currentTheme: currentTheme
  };
}());




















