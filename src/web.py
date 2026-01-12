from flask import Flask, render_template_string, request, redirect, url_for
from src.db import init_db, get_conn

app = Flask(__name__)

# Asegura que la DB y la tabla existen al arrancar
init_db()

HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Monsters</title>
  </head>
  <body>
    <h1>Registro de Monsters</h1>
    <p>Esto es una lista sacada de SQLite.</p>
    <ul>
      {% for m in monsters %}
        <li><b>{{m[1]}}</b> - {{m[2]}} ({{m[3]}}ml) — {{m[4]}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
"""

@app.get("/")
def home():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, name, flavor, size_ml, created_at
            FROM monsters
            ORDER BY created_at DESC
        """)
        monsters = cur.fetchall()

    return render_template_string(HTML, monsters=monsters)

HTML_NEW = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Añadir Monster</title>
  </head>
  <body>
    <h1>Añadir Monster</h1>
    <p><a href="/new">Añadir nuevo</a></p>
    <form method="post">
      <label>Nombre</label><br>
      <input name="name" required><br><br>

      <label>Sabor</label><br>
      <input name="flavor" required><br><br>

      <label>Tamaño (ml)</label><br>
      <input name="size_ml" type="number" required><br><br>

      <button type="submit">Guardar</button>
    </form>

    <p><a href="/">Volver</a></p>
  </body>
</html>
"""

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        name = request.form["name"].strip()
        flavor = request.form["flavor"].strip()
        size_ml = int(request.form["size_ml"])

        with get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO monsters (name, flavor, size_ml)
                VALUES (?, ?, ?)
            """, (name, flavor, size_ml))
            conn.commit()

        return redirect(url_for("home"))

    return render_template_string(HTML_NEW)
