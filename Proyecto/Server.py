import socket 
import threading

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DESCONECTAOD"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(4)  # solo deja conectar a cuatro jugadores

def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr} comentado!.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Mensaje recibido ".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[INICIANDO ] Servidor se esta ejecutando en {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXION ACTIVA] {threading.activeCount() - 1}")


print("[INICIANDO ] servidor esta ejecutando...")
start()