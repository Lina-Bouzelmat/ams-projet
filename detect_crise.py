import sqlite3
from datetime import datetime, timedelta
from envoyer_email import envoyer_email, generer_message, recuperer_derniere_mesure

SEUIL_CPU = 80.0
SEUIL_RAM = 90.0
DUREE_MINUTES = 5

db_path = "/home/uapv2202351/data/systeme_monitor.db"
template_path = "/home/uapv2202351/scripts/template_email.txt"

connexion = sqlite3.connect(db_path)
cursor = connexion.cursor()
limite = datetime.now() - timedelta(minutes=DUREE_MINUTES)
cursor.execute("""
    SELECT timestamps, cpu_usage, ram_usage FROM system_metrics
    WHERE timestamps >= ?
""", (limite.strftime('%Y-%m-%d %H:%M:%S'),))
lignes = cursor.fetchall()
connexion.close()

alerte = False
for ts, cpu, ram in lignes:
    if cpu > SEUIL_CPU or ram > SEUIL_RAM:
        print(f"CRISE détectée à {ts} : CPU={cpu}%, RAM={ram}%")
        alerte = True

if alerte:
    cpu, ram = recuperer_derniere_mesure(db_path)
    contenu = generer_message(cpu, ram, template_path)
    envoyer_email(contenu)
else:
    print("Aucune crise détectée sur les lignes", len(lignes), "dernière valeur.")
