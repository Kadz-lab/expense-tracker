import sqlite3

def connect_db():
    conn = sqlite3.connect("expenses.db", check_same_thread=False)
    return conn

def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS expenses(
                date TEXT,
                amount REAL,
                category TEXT,
                description TEXT)""")
    conn.commit()

def add_expense(date, amount, category, description):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO expenses VALUES (?,?,?,?)",
              (date, amount, category, description))
    conn.commit()

def view_expenses():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    return c.fetchall()