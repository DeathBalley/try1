from src.db import init_db, get_conn

def add_monster():
    name = input("Nombre (ej: Monster): ").strip()
    flavor = input("Sabor (ej: Mango Loco): ").strip()
    size_ml = int(input("Tamaño ml (ej: 500): ").strip())
    quantity = int(input("Cantidad: ").strip())

    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO monsters (name, flavor, size_ml, quantity)
            VALUES (?, ?, ?, ?)
        """, (name, flavor, size_ml, quantity))
        conn.commit()

    print("✅ Añadido.\n")

def list_monsters():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, name, flavor, size_ml, quantity, created_at
            FROM monsters
            ORDER BY created_at DESC
        """)
        rows = cur.fetchall()

    if not rows:
        print("📭 Inventario vacío.\n")
        return

    print("\n--- Inventario ---")
    for r in rows:
        print(f"[{r[0]}] {r[1]} - {r[2]} ({r[3]}ml) x{r[4]} | {r[5]}")
    print("------------------\n")

def main():
    init_db()

    while True:
        print("1) Añadir Monster")
        print("2) Ver inventario")
        print("0) Salir")
        choice = input("> ").strip()

        if choice == "1":
            add_monster()
        elif choice == "2":
            list_monsters()
        elif choice == "0":
            break
        else:
            print("❌ Opción no válida.\n")

if __name__ == "__main__":
    main()
