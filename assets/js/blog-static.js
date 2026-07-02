(function () {
    var body = document.body;
    if (!body.classList.contains("blog-static-page")) return;
    var toggle = document.getElementById("blog-dark-toggle");
    if (toggle && window.__siteTheme) {
        toggle.addEventListener("click", function () {
            window.__siteTheme.toggleTheme();
        });
    }
})();
