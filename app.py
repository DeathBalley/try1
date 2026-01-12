from flask import Flask, render_template, request, send_file
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/pdf")
def generar_pdf():
    # 1) Recoger datos del formulario
    titulo = request.form.get("titulo", "").strip()
    subtitulo = request.form.get("subtitulo", "").strip()
    contenido = request.form.get("contenido", "").strip()

    # 2) Crear PDF en memoria
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # 3) Escribir contenido (simple y legible)
    y = height - 60

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, titulo or "Sin título")
    y -= 28

    c.setFont("Helvetica", 12)
    if subtitulo:
        c.drawString(50, y, subtitulo)
        y -= 24

    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Contenido:")
    y -= 18

    # 4) Texto multilínea (separado por saltos de línea)
    text = c.beginText(50, y)
    text.setFont("Helvetica", 12)
    for line in (contenido.splitlines() if contenido else [""]):
        text.textLine(line)

    c.drawText(text)

    c.showPage()
    c.save()

    # 5) Devolver PDF como archivo descargable
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="plantilla.pdf",
        mimetype="application/pdf",
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
