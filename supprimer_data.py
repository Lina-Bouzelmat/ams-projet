import sqlite3

db_path = "/home/uapv2202351/data/systeme_monitor.db"
connexion = sqlite3.connect(db_path)
cursor = connexion.cursor()

def purge(table):
	cursor.execute(f"SELECT COUNT(*) FROM {table}")
	total = cursor.fetchone()[0]

	if total > 20:
		print(f" {table} contient {total} ligne - suppression des 5 plus anciennes..")
		cursor.execute(f"""
			DELETE FROM {table}
			WHERE id IN (
				SELECT id FROM {table}
				ORDER BY id ASC
				LIMIT 5
			)
		""")
		connexion.commit()
	else:
		print(f"{table} OK ({total} lignes)")

purge("system_metrics")
purge("alerts")

connexion.close()
