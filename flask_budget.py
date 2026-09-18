from flask import Flask , render_template, request , redirect
import sqlite3

app = Flask(__name__) 

def init_db():
    conn =sqlite3.connect("budget.db")
    cursor = conn.cursor()
#Income table 
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS income(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount REAL NOT NULL,
                   source TEXT NOT NULL,
                   date TEXT NOT NULL,
                   notes TEXT
                   )
                   """)
    #Expense Table 
    
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS expense(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   date TEXT NOT NULL,
                   notes TEXT
                   )
                   """)
    
    



    conn.commit()
    conn.close()


@app.route("/")

def home():
    conn = sqlite3.connect("budget.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

# Get all income 
    cursor.execute("SELECT * FROM income ORDER BY id DESC")
    income = cursor.fetchall()

    #Get all Expenses
    cursor.execute("SELECT * FROM expense ORDER BY id DESC")
    expenses = cursor.fetchall()

    conn.close()
    return render_template("dashboard.html", income=income, expenses=expenses)

@app.route("/add-income", methods=["GET", "POST"])
def add_income():

    if request.method == "POST": 
        amount = request.form["amount"]
        source = request.form["source"]
        date = request.form["date"]
        notes = request.form["notes"]

        conn = sqlite3.connect("budget.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO income (amount, source, date, notes)
            VALUES (?, ?, ?, ?)
        """, (amount, source, date, notes))

        conn.commit()
        conn.close()

        return redirect ("/")
    return render_template("add_income.html") 


@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST": 
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]
        notes = request.form["notes"]

        conn = sqlite3.connect("budget.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO expense (amount, category, date, notes)
            VALUES (?, ?, ?, ?)
        """, (amount, category, date, notes))

        conn.commit()
        conn.close()

        return redirect ("/")
    return render_template("add_expense.html") 



@app.route("/about")
def about():
    return "About page"


if __name__ == "__main__":
    init_db()
    app.run(debug = True) 
