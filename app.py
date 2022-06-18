from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contatos")
def contato():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)
