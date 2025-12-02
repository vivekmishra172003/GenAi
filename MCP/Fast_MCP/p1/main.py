from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "expense.db")

mcp = FastMCP("ExpenseTracker",port=5000)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT,
                note Text DEFAULT ''
            )
        """)

init_db()


@mcp.tool()
def add_expense(date: str, amount: float, category: str, subcategory: str = None, note: str = None) -> str:
    """Add an expense to the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("""
            INSERT INTO expenses (date, amount, category, subcategory, note)
            VALUES (?, ?, ?, ?, ?)
        """, (date, amount, category, subcategory, note))
        expense_id = cursor.lastrowid
    return {"status":"ok","id":expense_id}


@mcp.tool()
def list_expenses() -> list:
    """List all expenses in the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT * FROM expenses")
        return [dict(row) for row in cursor.fetchall()]
    

if __name__ == "__main__":
    mcp.run()

