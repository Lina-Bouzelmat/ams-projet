from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
        <h1>Interface de visualisation AMS</h1>
        <ul>
            <li><a href="/graph_cpu">Graphique CPU</a></li>
            <li><a href="/graph_ram">Graphique RAM</a></li>
            <li><a href="/graph_alerts">Graphique Alertes</a></li>
        </ul>
    """)

@app.route('/graph_cpu')
def graph_cpu():
    return send_file('/home/uapv2202351/graphs/cpu_graph.png', mimetype='image/png')

@app.route('/graph_ram')
def graph_ram():
    return send_file('/home/uapv2202351/graphs/ram_graph.png', mimetype='image/png')

@app.route('/graph_alerts')
def graph_alerts():
    return send_file('/home/uapv2202351/graphs/alerts_graph.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
