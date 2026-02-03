from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- RUTAS DE NAVEGACIÓN ---

@app.route('/')
def index():
    """Renderiza la Landing Page principal."""
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    """Renderiza la interfaz del mapa interactivo."""
    return render_template('mapa.html')


# --- ENDPOINTS DE API ---

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    """
    Recibe coordenadas desde el mapa y las procesa.
    """
    try:
        # Obtenemos los datos JSON enviados por el fetch
        datos = request.get_json()
        
        # Validación de seguridad: Verificar que los datos existan
        if not datos:
            return jsonify({"status": "error", "message": "No se recibieron datos"}), 400
            
        lat = datos.get('lat')
        lng = datos.get('lng')

        # Verificamos que las coordenadas no sean None
        if lat is None or lng is None:
            return jsonify({"status": "error", "message": "Coordenadas incompletas"}), 400

        # Simulación de guardado (Aquí conectarías tu DB en el futuro)
        # Log en consola para verificar la recepción en tiempo real
        print(f"--- NUEVO PUNTO REGISTRADO EN RUTASTJ ---")
        print(f"Ubicación: [{lat}, {lng}]")
        print(f"----------------------------------------")

        # Respuesta exitosa para el frontend
        return jsonify({
            "status": "success", 
            "message": "Punto guardado en la red de RutasTj",
            "data": {"lat": lat, "lng": lng}
        }), 200

    except Exception as e:
        # Captura cualquier error inesperado
        print(f"Error en el servidor: {str(e)}")
        return jsonify({"status": "error", "message": "Error interno del servidor"}), 500

if __name__ == '__main__':
    # Usar 0.0.0.0 permite conexiones desde cualquier IP local si es necesario
    app.run(debug=True, host='127.0.0.1', port=5000)