import sqlite3
from datetime import datetime

with open("/home/uapv2202351/data/last_alert.txt", "r") as f:
	alert_text = f.read().strip()

if alert_text:
	connexion = sqlite3.connect("/home/uapv2202351/data/systeme_monitor.db")
	cursor = connexion.cursor()

	cursor.execute("SELECT COUNT (*) FROM alerts WHERE alert_text = ?", (alert_text,))
	exists = cursor.fetchone()[0]

	if exists == 0:
		cursor.execute("INSERT INTO alerts (timestamps, alert_text) VALUES (?,?)", (datetime.now(),alert_text))
		connexion.commit()

		print("Alerte CERT enregistrée: ", alert_text)
	else:
		print("Alerte déjà enregistrée")

	connexion.close()
else:
	print("Aucune nouvelle alert trouvée")

