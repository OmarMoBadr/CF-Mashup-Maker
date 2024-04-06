classNames = [
  "second-level-menu",
  "button-up",
  "menu-box",
  "input-output-copier",
  // "time-limit",
  // "memory-limit",
  "input-file",
  "output-file",
  "epigraph"
];
ids = ["header", "footer", "sidebar"];

const elements = document.querySelectorAll("." + classNames.join(",."));
elements.forEach(function (element) {
  element.remove();
});

ids.forEach(function (id) {
  const element = document.getElementById(id);
  if (element) {
    element.remove();
  }
});

const brElements = document.querySelectorAll("br");
brElements.forEach(function (br) {
  if (br.style.height == "3em") {
    br.remove();
  }
});

const element1 = document.getElementById("pageContent");
element1.style.margin = "0";
element1.style.paddingTop = "0";

const element = document.getElementById("pageContent");
// content-with-sidebar
element.style.marginRight = "16em";
element.classList.remove('content-with-sidebar');

// style="margin-top:15em;"
