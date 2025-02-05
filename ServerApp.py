from flask import Flask, request
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes de origen cruzado

@app.route('/log', methods=['POST'])
def recibir_log():
    data = request.json
    print(f"Tecla presionada: {data}")
    return {"status": "recibido"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)