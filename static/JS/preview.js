const titulo = document.getElementById("titulo");
const subtitulo = document.getElementById("subtitulo");
const contenido = document.getElementById("contenido");

const pTitulo = document.getElementById("p_titulo");
const pSubtitulo = document.getElementById("p_subtitulo");
const pContenido = document.getElementById("p_contenido");

function sync() {
  pTitulo.textContent = titulo.value.trim() || "Sin título";
  pSubtitulo.textContent = subtitulo.value.trim();
  pContenido.textContent = contenido.value || "";
}

titulo.addEventListener("input", sync);
subtitulo.addEventListener("input", sync);
contenido.addEventListener("input", sync);

// inicial
sync();
