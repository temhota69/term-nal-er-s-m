import socket
import threading

# Ayarlar
HOST = '0.0.0.0' # Tüm bağlantıları kabul et
PORT = 1234      # İstediğin portu seç

clients = []

def encrypt_message(msg):
    # Kendi şifreleme mantığını buraya ekle
    return msg # Şimdilik düz metin

def decrypt_message(msg):
    # Kendi çözme mantığını buraya ekle
    return msg

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            # Mesaj geldiğinde burada işleyebilirsin
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Sunucu {PORT} portunda dinlemede...")

    while True:
        client, address = server.accept()
        print(f"{str(address)} bağlandı!")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

start_server()