import pyodbc
connect=None
def get_db_connection():
    conn_str = (
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-ON6R1A5\\MSSQLSERVER01;'
        'DATABASE=RecipeDB;'
        'Trusted_Connection=yes;'
    )
    return pyodbc.connect(conn_str)

def read_recipes(category_name=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT r.recipe_id, r.recipe_name, r.instructions, c.category_name 
            FROM recipes r
            JOIN categories c ON r.category_id = c.category_id
        """

        if category_name:
            query += " WHERE c.category_name = ?"
            cursor.execute(query, (category_name,))
        else:
            cursor.execute(query)

        rows = cursor.fetchall()
        conn.close()

        return [{"id": int(r[0]), "name": str(r[1]), "instructions": str(r[2]), "category": str(r[3])} for r in rows]
    except Exception as e:
        print(f"Database Error: {e}")
        return []


def get_recipe_by_id(recipe_id):
    """שולף מתכון כולל הוראות - לדרישה מס' 2"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT r.recipe_id, r.recipe_name, r.instructions, c.category_name 
            FROM recipes r
            JOIN categories c ON r.category_id = c.category_id
            WHERE r.recipe_id = ?
        """
        cursor.execute(query, (recipe_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "instructions": row[2], "category": row[3]}
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def add_recipe(name, instructions, cat_id, u_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (recipe_name, instructions, category_id, user_id) VALUES (?, ?, ?, ?)",
                   (name, instructions, cat_id, u_id))
    conn.commit()
    conn.close()
    return True

def delete_recipe(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM recipes WHERE recipe_id = ?", (id,))
        count = cursor.rowcount
        conn.commit()
        conn.close()
        return count > 0
    except Exception as e:
        print(f"Error deleting recipe: {e}")
        return False


def update_recipe(recipe_id, name=None, instructions=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if name and instructions:
            cursor.execute("UPDATE recipes SET recipe_name = ?, instructions = ? WHERE recipe_id = ?",
                           (name, instructions, recipe_id))
        elif name:
            cursor.execute("UPDATE recipes SET recipe_name = ? WHERE recipe_id = ?", (name, recipe_id))
        elif instructions:
            cursor.execute("UPDATE recipes SET instructions = ? WHERE recipe_id = ?", (instructions, recipe_id))

        count = cursor.rowcount
        conn.commit()
        conn.close()
        return count > 0
    except Exception as e:
        print(f"Error updating: {e}")
        return False


