import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Yazdığımız satırı bozmamak için başa \r ekliyoruz
                print(f"\r{message}")
                print("Mesajınız: ", end="", flush=True)
            else:
                break
        except:
            print("\n[X] Sunucu bağlantısı koptu.")
            break

def start_client():
    # GİRİŞ EKRANI
    print("--- TERMİNAL CHAT GİRİŞ ---")
    target_ip = input("Bağlanılacak IP: ")
    port = int(input("Port (Örn: 1234): "))
    name = input("Kullanıcı Adınız: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target_ip, port))
        print(f"\n[!] {target_ip}:{port} adresine bağlandınız. Sohbet başlıyor...")
    except Exception as e:
        print(f"[X] Bağlantı hatası: {e}")
        return

    # Mesaj alma thread'ini başlat
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # Mesaj gönderme döngüsü
    try:
        while True:
            msg = input("Mesajınız: ")
            if msg.lower() == 'exit':
                break
            if msg:
                # Mesajı "İsim: Mesaj" formatında gönderiyoruz
                full_message = f"[{name}]: {msg}"
                client.send(full_message.encode('utf-8'))
    except KeyboardInterrupt:
        print("\nÇıkış yapılıyor...")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
