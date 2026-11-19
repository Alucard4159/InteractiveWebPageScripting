(function () {
  if (document.querySelector(".side-portraits")) {
    return;
  }

  var base = "";
  var scripts = document.getElementsByTagName("script");
  for (var i = 0; i < scripts.length; i++) {
    var src = scripts[i].src || "";
    var marker = "/includes/side-portraits.js";
    var idx = src.lastIndexOf(marker);
    if (idx === -1) {
      idx = src.lastIndexOf("includes/side-portraits.js");
      if (idx !== -1) {
        base = src.slice(0, idx);
        break;
      }
    } else {
      base = src.slice(0, idx + 1);
      break;
    }
  }

  var wrap = document.createElement("div");
  wrap.className = "side-portraits";
  wrap.setAttribute("aria-hidden", "true");
  wrap.innerHTML =
    '<img class="portrait portrait-left" src="' + base + 'includes/Strahd-1.jpg" alt="">' +
    '<img class="portrait portrait-right" src="' + base + 'includes/Strahd-2.jpg" alt="">';
  document.body.prepend(wrap);
})();
