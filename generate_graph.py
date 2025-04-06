import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Connexion à la base
conn = sqlite3.connect("/home/uapv2202351/data/systeme_monitor.db")
cursor = conn.cursor()

# Récupérer les 50 dernières mesures
cursor.execute("""
    SELECT timestamps, cpu_usage, ram_usage 
    FROM system_metrics 
    ORDER BY id DESC LIMIT 50
""")
data = cursor.fetchall()
conn.close()

# Organiser les données
timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in reversed(data)]
cpu = [row[1] for row in reversed(data)]
ram = [row[2] for row in reversed(data)]

# Création du graphique
plt.figure(figsize=(10, 5))
plt.plot(timestamps, cpu, label="CPU %")
plt.plot(timestamps, ram, label="RAM %")
plt.xlabel("Horodatage")
plt.ylabel("Utilisation (%)")
plt.title("Évolution de la charge CPU / RAM")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Sauvegarde du graphique
plt.savefig("/home/uapv2202351/logs/evolution_graph.png")
print(" Graphique généré : logs/evolution_graph.png")
