import sqlite3
from datetime import datetime, timedelta
from envoyer_email import envoyer_email, generer_message, recuperer_derniere_mesure

# === Paramètres configurables ===
SEUIL_CPU = 80.0  # en %
SEUIL_RAM = 90.0  # en %
DUREE_MINUTES = 5  # analyse sur les 5 dernières minutes

# === Chemins utiles ===
db_path = "/home/uapv2202351/data/systeme_monitor.db"
template_path = "/home/uapv2202351/scripts/template_email.txt"
destinataire = "lina.bouzelmat@alumni.univ-avignon.fr"

# === Récupération des données ===
limite = datetime.now() - timedelta(minutes=DUREE_MINUTES)

connexion = sqlite3.connect(db_path)
cursor = connexion.cursor()
cursor.execute("""
    SELECT timestamps, cpu_usage, ram_usage
    FROM system_metrics
    WHERE timestamps >= ?
""", (limite.strftime("%Y-%m-%d %H:%M:%S"),))
lignes = cursor.fetchall()
connexion.close()

# === Analyse des mesures ===
alerte = False
for ts, cpu, ram in lignes:
    if cpu > SEUIL_CPU or ram > SEUIL_RAM:
        print(f"CRISE détectée à {ts} : CPU={cpu}%, RAM={ram}%")
        alerte = True
        break

# === Envoi de l'alerte si besoin ===
if alerte:
    cpu, ram = recuperer_derniere_mesure(db_path)
    contenu = generer_message(cpu, ram, template_path)
    envoyer_email(contenu, destinataire)
    print("MAIL ENVOYÉ")
else:
    print("Aucune crise détectée.")
