from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Aqui você pode fornecer dados dinâmicos para o template, se necessário
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
