from flask import Flask, send_file, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
        <h1>Interface de visualisation AMS</h1>
        <p><a href="/graph">Voir le graphique d'évolution CPU/RAM</a></p>
        <img src="/graph" alt="Graphe CPU/RAM">
    """)

@app.route('/graph')
def graph():
    return send_file('/home/uapv2202351/graphs/evolution_graph.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
