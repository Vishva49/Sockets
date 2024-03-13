import socket as s
from threading import Thread
HOST = '127.0.0.1'
PORT = 3000

class ASPincomingThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        self.conn.sendall("Welcome to my Server\n".encode())
        data = self.conn.recv(1024)
        while data:
            print("{} : ".format(self.addr[0]) + data.decode(),end="")
            data = self.conn.recv(1024)


sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()
while True:
    print("Waiting for new conection...")
    conn,addr = sck.accept()
    print("connection received from {}:{}".format(addr[0],addr[1]))
    ASPincomingThread(conn,addr).start()
