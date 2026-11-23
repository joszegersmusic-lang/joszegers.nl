(function () {
  var root = document.documentElement;
  var lang = root.lang || "nl";
  var labels = {
    nl: { dark: "Donkere weergave", light: "Lichte weergave", open: "Menu", close: "Sluiten" },
    en: { dark: "Dark mode", light: "Light mode", open: "Menu", close: "Close" },
    de: { dark: "Dunkle Ansicht", light: "Helle Ansicht", open: "Menü", close: "Schließen" }
  }[lang] || {};

  /* Weergave: volgt het systeem, tenzij de bezoeker zelf kiest */
  var themeButton = document.querySelector(".theme");
  var media = window.matchMedia("(prefers-color-scheme: dark)");

  function currentTheme() {
    return root.dataset.theme || (media.matches ? "dark" : "light");
  }
  function syncThemeButton() {
    if (!themeButton) return;
    var dark = currentTheme() === "dark";
    themeButton.setAttribute("aria-pressed", dark ? "true" : "false");
    themeButton.setAttribute("aria-label", dark ? labels.light : labels.dark);
    themeButton.title = dark ? labels.light : labels.dark;
  }
  if (themeButton) {
    themeButton.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
      syncThemeButton();
    });
    if (media.addEventListener) media.addEventListener("change", syncThemeButton);
    syncThemeButton();
  }

  /* Menu op kleine schermen */
  var menuButton = document.querySelector(".menu-button");
  var menu = document.getElementById("menu");
  function setMenu(open) {
    menu.classList.toggle("is-open", open);
    menuButton.setAttribute("aria-expanded", open ? "true" : "false");
    menuButton.textContent = open ? labels.close : labels.open;
  }
  if (menuButton && menu) {
    menuButton.addEventListener("click", function () {
      setMenu(!menu.classList.contains("is-open"));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        setMenu(false);
        menuButton.focus();
      }
    });
  }

  /* Lijn onder de kopbalk zodra er gescrold is */
  var bar = document.querySelector(".bar");
  function onScroll() { bar.classList.toggle("is-scrolled", window.scrollY > 8); }
  if (bar) { window.addEventListener("scroll", onScroll, { passive: true }); onScroll(); }

  /* Markeer in het menu welke sectie in beeld is */
  if ("IntersectionObserver" in window && menu) {
    var links = {};
    menu.querySelectorAll('a[href^="#"]').forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = links[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          Object.keys(links).forEach(function (k) { links[k].removeAttribute("aria-current"); });
          link.setAttribute("aria-current", "true");
        } else {
          link.removeAttribute("aria-current");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    document.querySelectorAll(".part[id]").forEach(function (s) { observer.observe(s); });
  }

  var year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
})();
