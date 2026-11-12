(function () {
  if (document.querySelector(".side-portraits")) {
    return;
  }

  var wrap = document.createElement("div");
  wrap.className = "side-portraits";
  wrap.setAttribute("aria-hidden", "true");
  wrap.innerHTML =
    '<img class="portrait portrait-left" src="includes/Strahd-1.jpg" alt="">' +
    '<img class="portrait portrait-right" src="includes/Strahd-2.jpg" alt="">';
  document.body.prepend(wrap);
})();
