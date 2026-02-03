from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Landing Page de la Actividad 1
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    # Nueva vista del mapa de la Actividad 2
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)