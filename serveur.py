import socket

host = '0.0.0.0'  # écoute toutes les IP
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print("🟢 Serveur en attente de connexion...")
    conn, addr = s.accept()
    with conn:
        print(f"🟠 Connecté à {addr}")
        data = conn.recv(1024).decode()
        print(f"📥 Données reçues : {data}")
