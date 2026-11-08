from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Sistema de Gestión de E-commerce</h1>
    <p>Bienvenido a nuestra tienda virtual.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)