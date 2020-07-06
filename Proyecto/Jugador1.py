import socket
import subprocess

out = subprocess.Popen(['ipconfig'],stdout=subprocess.PIPE)
stdout,stderr = out.communicate()
i=iter(stdout.splitlines())
for linea in i:
    if str(linea).find("Wi-Fi") !=-1:
        for linea2 in i:
            if str(linea2).find("IPv4") !=-1:
                print(str(linea2).split(':')[1].strip()[:-1])
                SERVER=str(linea2).split(':')[1].strip()[:-1]

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)