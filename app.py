from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hola amigo flask"

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)
