import sqlite3
import os
import psutil
from datetime import datetime

db_path = "/home/uapv2202351/data/systeme_monitor.db"

connexion = sqlite3.connect(db_path)
cursor = connexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS system_metrics (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
	cpu_usage REAL,
	ram_usage REAL
)
""")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent

cursor.execute("INSERT INTO system_metrics (cpu_usage,ram_usage) VALUES (?,?)",(cpu,ram))

connexion.commit()
connexion.close()

print(f"Donnée insérer : CPU={cpu}%, RAM={ram}%")

