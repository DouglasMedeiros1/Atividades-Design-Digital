from flask import Flask, render_template, request


app = Flask("__name__")

@app.route('/')
def base():
    return render_template("home.html")

@app.route('/Hobbies')
def hobbies():
    return render_template("hobbies.html")

@app.route('/HistoricoAcademico')
def historico():
    return render_template("historico.html")


if "__name__" == '_main_':
    app.run()