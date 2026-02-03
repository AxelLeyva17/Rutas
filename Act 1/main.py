from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Esto buscará automáticamente en la carpeta 'templates' el archivo 'index.html'
    return render_template('index.html')

@app.route('/mapa')
def ver_mapa():
    return "Aquí se mostrará el mapa interactivo de RutasTj"

if __name__ == '__main__':
    app.run(debug=True, port=5000)