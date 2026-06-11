(function () {
  var container = document.getElementById('shared-site-footer');
  if (!container) return;

  if (!document.getElementById('shared-site-footer-style')) {
    var style = document.createElement('style');
    style.id = 'shared-site-footer-style';
    style.textContent = [
      '.site-footer-widget { background: transparent !important; box-shadow: none !important; padding: 0 !important; border: 0 !important; }',
      '.site-footer-widget .footer-logo-box { margin-bottom: 18px; }',
      '.site-footer-widget .footer-social { display: none !important; }',
      '.site-footer-widget + .site-footer-widget { margin-top: 30px; }',
      '.footer-area .row > div { margin-bottom: 24px; }',
      '.footer-area .row > div:last-child { margin-bottom: 0; }',
      '@media (min-width: 992px) { .footer-area .row > div { margin-bottom: 0; } }',
      'body[data-theme="dark"] .site-footer-widget { background: transparent !important; box-shadow: none !important; border: 0 !important; }',
      'body[data-theme="dark"] .site-footer-copyright { border-top: 1px solid rgba(148,163,184,.12); }'
    ].join('');
    document.head.appendChild(style);
  }

  var htmlLang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
  var lang = 'en';
  if (htmlLang.indexOf('zh-cn') === 0) lang = 'zh-cn';
  else if (htmlLang.indexOf('zh-hk') === 0 || htmlLang.indexOf('zh-tw') === 0) lang = 'zh-hk';

  var copy = {
    en: {
      desc: 'Hong Kong-based strategist, investor, and software builder working across market growth, investment research, and technical delivery. My Email: fengyuwang1@outlook.com',
      quickLinks: 'Quick Links',
      about: 'About Me',
      contact: 'Contact',
      services: 'Service Offerings',
      portfolio: 'Tech',
      contactInfo: 'Contact Information',
      email: 'Email',
      location: 'Location',
      locationValue: 'Mong Kok, Hong Kong',
      copyright: '2026 - Fengyu WANG \'Steve\'. All Rights Reserved.',
      homeHref: '/en/index.html'
    },
    'zh-cn': {
      desc: '\u5e38\u9a7b\u9999\u6e2f\uff0c\u540c\u65f6\u4ece\u4e8b\u5e02\u573a\u7b56\u7565\u3001\u6295\u8d44\u7814\u7a76\u4e0e\u8f6f\u4ef6\u4ea4\u4ed8\u7684\u5de5\u4f5c\u8005\u3002\u64c5\u957f\u7528\u6280\u672f\u548c\u6570\u636e\u63a8\u52a8\u589e\u957f\u4e0e\u6548\u7387\u3002\u6211\u7684\u90ae\u7bb1\uff1afengyuwang1@outlook.com',
      quickLinks: '\u5feb\u901f\u94fe\u63a5',
      about: '\u5173\u4e8e\u6211',
      contact: '\u8054\u7cfb',
      services: '\u670d\u52a1\u9879\u76ee',
      portfolio: '\u6280\u672f',
      contactInfo: '\u8054\u7cfb\u4fe1\u606f',
      email: '\u7535\u5b50\u90ae\u4ef6',
      location: '\u6240\u5728\u5730',
      locationValue: 'Mong Kok, Hong Kong',
      copyright: '2026 - Fengyu WANG \'Steve\'. All Rights Reserved.',
      homeHref: '/zh-cn/index.html'
    },
    'zh-hk': {
      desc: '\u5e38\u99d0\u9999\u6e2f\uff0c\u540c\u6642\u5f9e\u4e8b\u5e02\u5834\u7b56\u7565\u3001\u6295\u8cc7\u7814\u7a76\u8207\u8edf\u4ef6\u4ea4\u4ed8\u7684\u5de5\u4f5c\u8005\u3002\u64c5\u9577\u7528\u6280\u8853\u548c\u6578\u64da\u63a8\u52d5\u589e\u9577\u8207\u6548\u7387\u3002\u6211\u7684\u90f5\u7bb1\uff1afengyuwang1@outlook.com',
      quickLinks: '\u5feb\u901f\u93c8\u63a5',
      about: '\u95dc\u65bc\u6211',
      contact: '\u806f\u7d61',
      services: '\u670d\u52d9\u9805\u76ee',
      portfolio: '\u6280\u8853',
      contactInfo: '\u806f\u7d61\u4fe1\u606f',
      email: '\u96fb\u5b50\u90f5\u4ef6',
      location: '\u6240\u5728\u5730',
      locationValue: 'Mong Kok, Hong Kong',
      copyright: '2026 - Fengyu WANG \'Steve\'. All Rights Reserved.',
      homeHref: '/zh-hk/index.html'
    }
  };

  var labels = copy[lang];
  var home = labels.homeHref;

  container.outerHTML = [
    '<section id="contact" class="footer-subscribe-wrapper"><div class="footer-area section-padding">',
    '  <div class="container">',
    '    <div class="row">',
    '      <div class="col-lg-4 col-md-6 col-sm-6">',
    '        <div class="single-footer-widget site-footer-widget footer-brand-column">',
    '          <div class="footer-logo-box"><img src="/assets/img/logo.png" class="white-logo" alt="logo"></div>',
    '          <p>' + labels.desc + '</p>',
    '        </div>',
    '      </div>',
    '      <div class="col-lg-2 offset-lg-1 col-md-6 col-sm-6">',
    '        <div class="single-footer-widget site-footer-widget">',
    '          <div class="footer-heading"><h3>' + labels.quickLinks + '</h3></div>',
    '          <ul class="footer-quick-links">',
    '            <li><a href="' + home + '#about">' + labels.about + '</a></li>',
    '            <li><a href="' + home + '#contact">' + labels.contact + '</a></li>',
    '            <li><a href="' + home + '#services">' + labels.services + '</a></li>',
    '            <li><a href="' + home.replace("index.html", "portfolio.html") + '">' + labels.portfolio + '</a></li>',
    '            <li><a href="https://www.bilibili.com/video/BV1oW4y1i7qf" target="_blank" rel="noopener noreferrer" style="font-style:italic;font-weight:700;">' + (lang === 'en' ? '&ldquo;Think different.&rdquo;' : (lang === 'zh-cn' ? '&ldquo;不同凡想&rdquo;' : '\u300c不同凡想\u300d')) + '</a></li>',
    '          </ul>',
    '        </div>',
    '      </div>',
    '      <div class="col-lg-4 offset-lg-1 col-md-6 col-sm-6">',
    '        <div class="single-footer-widget site-footer-widget">',
    '          <div class="footer-heading"><h3>' + labels.contactInfo + '</h3></div>',
    '          <div class="footer-info-contact"><h5>' + labels.email + '</h5><span><a href="mailto:fengyuwang1@outlook.com">fengyuwang1@outlook.com</a></span></div>',
    '          <div class="footer-info-contact"><h5>' + labels.location + '</h5><span>' + labels.locationValue + '</span></div>',
    '        </div>',
    '      </div>',
    '    </div>',
    '  </div>',
    '</div></section>',
    '<div class="copyright-area site-footer-copyright">',
    '  <div class="container"><div class="row align-items-center"><div class="col-lg-12 col-md-12"><p><i class="far fa-copyright"></i> <span>' + labels.copyright + '</span></p></div></div></div>',
    '</div>'
  ].join('');
}());

