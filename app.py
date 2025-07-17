from flask import Flesk, render_template

app = Flesk(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def sobre():
    return render_template("sobre.html")

@app.route("/")
def contato():
    return render_template("contato.html")

if __name__ == '__main__':
    app.run(debug=True)