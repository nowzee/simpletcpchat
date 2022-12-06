#import library
import socket
import threading

name = input('choisi un nom utilisateur')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6666))

def receive():
    while True:
        try:
            mss = client.recv(1024).decode('utf-8')
            print(mss)
        except WindowsError as f:
            print(f)
            break
def send():
    client.send('r'.encode('utf-8'))
    while True:
        mss = f'{name}: {input("")}'
        client.send(mss.encode())
receive_thread = threading.Thread(target=receive)
receive_thread.start()
sends = threading.Thread(target=send)
sends.start()
