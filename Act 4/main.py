from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- RUTAS DE VISTAS (PÁGINAS) ---

@app.route('/')
def index():
    """Carga la Landing Page (Actividad 1)"""
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    """Carga el Mapa con la Lista Lateral (Actividad 4)"""
    return render_template('mapa.html')


# --- RUTAS DE API (BACKEND) ---
# Nota: Aunque tu HTML actual usa simulación (JS), dejamos esto listo
# por si quieres conectar la base de datos más adelante.

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    try:
        datos = request.get_json()
        if not datos:
            return jsonify({"status": "error", "message": "Sin datos"}), 400
            
        # Aquí imprimiríamos las coordenadas en la consola de Python
        print(f"📍 Servidor recibió: {datos}")
        
        return jsonify({"status": "success", "message": "Guardado"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # host='0.0.0.0' ayuda a veces con problemas de conexión local
    app.run(debug=True, host='127.0.0.1', port=5000)