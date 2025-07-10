from flask import Flask, session, redirect, url_for
import GuessNumber

app = Flask(__name__)
app.secret_key = "rahasia"

app.add_url_rule("/", view_func=GuessNumber.SetNumber, methods=["GET", "POST"])
app.add_url_rule("/guenum", view_func=GuessNumber.GuessNum, methods=["GET", "POST"])

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("SetNumber"))

@app.route("/setnum")
def setNum():
    return GuessNumber.SetNumber

if __name__ == "__main__":
    app.run(debug=True)