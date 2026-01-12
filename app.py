from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # En Codespaces conviene 0.0.0.0 para exponer el puerto
    app.run(host="0.0.0.0", port=5000, debug=True)
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Generador PDF</title>
  </head>
  <body>
    <h1>Hola desde Flask </h1>
    <p>Si ves esto, la web funciona.</p>
  </body>
</html>
