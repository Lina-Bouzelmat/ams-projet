import smtplib
import ssl
import certifi
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuration du serveur SMTP
port = 465
smtp_server = "partage.univ-avignon.fr"
sender_email = "lina.bouzelmat@alumni.univ-avignon.fr"
receiver_email = "lina.bouzelmat@alumni.univ-avignon.fr"

try:
    from config import SMTP_PASSWORD
    password = SMTP_PASSWORD
except ImportError:
    password = input("Entrez votre mot de passe SMTP: ")

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

def envoyer_email(contenu):
    message = MIMEMultipart()
    message["Subject"] = "Alerte AMS - Situation de crise en cours"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(contenu, "plain"))

    context = ssl.create_default_context(cafile=certifi.where())
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("MAIL ENVOYÉEEE")

if __name__ == "__main__":
    db_path = "/home/uapv2202351/data/systeme_monitor.db"
    template_path = "/home/uapv2202351/scripts/template_email.txt"
    cpu, ram = recuperer_derniere_mesure(db_path)
    contenu = generer_message(cpu, ram, template_path)
    envoyer_email(contenu)