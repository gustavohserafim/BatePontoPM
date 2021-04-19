from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from Model.User import UserModel
from Model.Ponto import PontoModel
from os import environ

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]


@app.route("/")
def index():
    if "user_pin" in session:
        user_pin = session["user_pin"]
        user = UserModel.get(user_pin)
        if user:
            ponto_aberto = PontoModel().pontoAberto(user_pin)
            return render_template("ponto.html", user=user, ponto_aberto=ponto_aberto)
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user_pin"] = request.form["pin"]
        return redirect(url_for("index"))
    else:
        return render_template("auth.html")


@app.route("/ponto", methods=["POST"])
def ponto():
    r = request.get_json()
    PontoModel.baterPonto(r["user_pin"], r["tipo"])
    return jsonify({"result": "ok"}), 200


if __name__ == "__main__":
    app.run()
