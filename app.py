from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():   

    if request.method == 'POST':
        if request.form.get("add"):
            return redirect(url_for("add"))
        if request.form.get("search"):
            return redirect(url_for("search"))
        if request.form.get("display"):
            return redirect(url_for("display"))

    return render_template("index.html")

@app.route("/add", methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        studDf = pd.read_csv("students.csv")
        studDf.loc[len(studDf.index)] = [
            request.form['id'],
            request.form['name'],
            request.form['gender'],
            request.form['dob'],
            request.form['city'],
            request.form['state'],
            request.form['email'],
            request.form['qual'],
            request.form['stream']
        ]
        print(studDf)
        studDf.to_csv('students.csv', encoding='utf-8', index=False)
    return render_template("add.html")

@app.route("/search", methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_id = request.form['id']
        studDf = pd.read_csv("students.csv")
        print(studDf)
        rsltDf = studDf.loc[studDf['Student Id'] == int(search_id)]
        print(rsltDf)
        studList = rsltDf.values.tolist()
        return render_template("display.html", students=studList)
    return render_template("search.html")

@app.route("/display", methods = ['GET', 'POST'])
def display():
    studDf = pd.read_csv("students.csv")
    studList = studDf.values.tolist()
    return render_template("display.html", students=studList)


if __name__ == "__main__": 
    app.run()