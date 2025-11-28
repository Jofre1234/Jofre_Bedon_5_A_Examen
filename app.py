from flask import Flask

app = Flask(__name__)

# Configuración básica
app.config['JSON_AS_ASCII'] = False

# Ruta principal (Solo saludo)
@app.route('/')
def hello_world():
    return "¡Hola! Mi prueba final Jofre Bedón!"

if __name__ == '__main__':
    # IMPORTANTE: debug=False para que sea seguro y estable
    app.run(debug=False, host='0.0.0.0', port=1002)
