from flask import Flask, request, jsonify # type: ignore
import pytest # type: ignore
import sys

app = Flask(__name__)

# Ruta principal
@app.route('/')
def hello_world():
    return "¡buenos dias a todos!"



if __name__ == '__main__':
    if "test" in sys.argv:
        run_tests()  # Ejecuta las pruebas con: python app.py test
    else:
        # CAMBIO REALIZADO: Puerto 1002
        app.run(debug=True, host='0.0.0.0', port=1002)