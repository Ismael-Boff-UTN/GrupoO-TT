import socket, pickle
import threading
import subprocess


class Server:
    OK = bytes(1)

    def __init__(self):
        PORT = 5050
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((SERVER_IP, PORT))
        self.server.listen()
        print(f"Server esta escuchando en {SERVER_IP}")
        self.SERVER_IP = self.get_wifi_ip()

    def cliente_atender(self,conn,addr):
        data_variable = pickle.loads(conn.recv(4096))
        print(data_variable)
        return data_variable

    def loop(self):
        conn, addr = self.server.accept()
        #meter en loop principal
        thread = threading.Thread(target=self.cliente_atender,args=(conn,addr))
        thread.start()
        #conn.send(pickle.dumps("ok"))

    def get_wifi_ip(self):
        out = subprocess.Popen(['ipconfig'],stdout=subprocess.PIPE)
        stdout,stderr = out.communicate()
        i=iter(stdout.splitlines())
        for linea in i:
            if str(linea).find("Wi-Fi") !=-1:
                for linea2 in i:
                    if str(linea2).find("IPv4") !=-1:
                        SERVER_IP=str(linea2).split(':')[1].strip()[:-1]
                        return SERVER_IP