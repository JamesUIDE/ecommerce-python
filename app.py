from flask import Flask
from database.database import inicializar_base_datos

app = Flask(__name__)

inicializar_base_datos()


@app.route("/")
def inicio():
    return """
    <h1>Sistema de Gestión de E-commerce</h1>
    <p>Bienvenido a nuestra tienda virtual.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)