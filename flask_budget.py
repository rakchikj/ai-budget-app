from flask import Flask , render_template, request

app = Flask(__name__) 



@app.route("/")

def home():
    return render_template("dashboard.html")

@app.route("/add-income", methods=["GET", "POST"])
def add_income():

    if request.method == "POST": 
        amount = request.form["amount"]
        source = request.form["source"]
        date = request.form["date"]
        notes = request.form["notes"]

        print(amount)
        print(source)
        print(date)
        print(notes)
    return render_template("add_income.html")

@app.route("/about")
def about():
    return "About page"


if __name__ == '__main__':
    app.run(debug = True) 