import smtplib
import sqlite3
from email.mime.text import MIMEText
from datetime import datetime

# === CONFIGURATION ===
SMTP_SERVER = "partage.univ-avignon.fr"
SMTP_PORT = 465
EMAIL_FROM = "lina.bouzelmat@alumni.univ-avignon.fr"
EMAIL_TO = "lina.bouzelmat@alumni.univ-avignon.fr"
EMAIL_PASSWORD = "TON_MOT_DE_PASSE_ICI"  # remplace par ton mot de passe ENT

def recuperer_derniere_mesure(db_path):
    connexion = sqlite3.connect(db_path)
    cursor = connexion.cursor()
    cursor.execute("SELECT cpu_usage, ram_usage FROM system_metrics ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    connexion.close()
    return result

def generer_message(cpu, ram, template_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(template_path, "r") as f:
        contenu = f.read()
    contenu = contenu.replace("{{cpu}}", str(cpu))
    contenu = contenu.replace("{{ram}}", str(ram))
    contenu = contenu.replace("{{datetime}}", now)
    return contenu

def envoyer_email(contenu, destinataire):
    msg = MIMEText(contenu)
    msg["Subject"] = "Alerte AMS - Situation de crise en cours"
    msg["From"] = EMAIL_FROM
    msg["To"] = destinataire

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    db_path = "/home/uapv2202351/data/systeme_monitor.db"
    template_path = "/home/uapv2202351/scripts/template_email.txt"
    destinataire = EMAIL_TO

    cpu, ram = recuperer_derniere_mesure(db_path)
    contenu = generer_message(cpu, ram, template_path)
    envoyer_email(contenu, destinataire)

    print(" MAIL ENVOYÉ")
