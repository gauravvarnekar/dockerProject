from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vitthal")
def vitthal():
    return render_template(
        "vitthal.html",
        title="Vitthal",
        description=(
            "Vitthal, also known as Vithoba, is a Hindu god predominantly worshipped "
            "in Maharashtra and Karnataka. He is considered a form of Lord Vishnu or Krishna. "
            "Vitthal's image often shows him standing on a brick, holding a mace and a conch, symbolizing his divine power."
        ),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  # Change port if needed

