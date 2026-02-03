from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- PÁGINA DE INICIO (LANDING) ---
@app.route('/')
def index():
    return render_template('index.html')

# --- APLICACIÓN DE MAPA ---
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

# --- API DE GUARDADO (SIMULADA O REAL) ---
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    # Recibimos los datos para que no falle el fetch
    datos = request.get_json()
    print(f"✅ Punto guardado: {datos}")
    return jsonify({"status": "success", "message": "Guardado"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)