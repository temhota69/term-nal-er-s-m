import socket
import threading

# Ayarlar
target_ip = '192.168.43.111'
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_ip, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(f"\nMesaj: {message}")
        except:
            print("Bağlantı kesildi.")
            client.close()
            break

def send_messages():
    while True:
        msg = input("Siz: ")
        # Şifreleme fonksiyonunu buraya entegre edebilirsin
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()