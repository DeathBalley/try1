function fitText(el, minPt = 18, maxPt = 72) {
  el.style.fontSize = maxPt + "pt";
  const maxWidth = el.parentElement.clientWidth;

  let size = maxPt;
  while (el.scrollWidth > maxWidth && size > minPt) {
    size -= 1;
    el.style.fontSize = size + "pt";
  }
}

// ejemplo:
const nameBox = document.getElementById("nameBox");
nameBox.textContent = "NOMBRE LARGO DE PRUEBA";
fitText(nameBox);
