import socket
import sqlite3
from datetime import datetime

db_path = "/home/uapv2202351/scripts/data/systeme_monitor.db"
connexion = sqlite3.connect(db_path)
cursor = connexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS system_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    cpu_usage REAL,
    ram_usage REAL
)
""")

connexion.commit()
connexion.close()

host = "0.0.0.0"
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("Serveur en attente...")

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024).decode()
            machine_ip = addr[0]
            cpu, ram = data.replace("CPU=", "").replace(" RAM=", "").replace("%", "").split(",")
            
            print(f"[{machine_ip}] CPU={cpu}%, RAM={ram}%")
            
            connexion = sqlite3.connect(db_path)
            cursor = connexion.cursor()
            cursor.execute("INSERT INTO system_metrics (machine, cpu_usage, ram_usage) VALUES (?, ?, ?)", (machine_ip, float(cpu), float(ram)))
            connexion.commit()
            connexion.close()

