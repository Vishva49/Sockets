import socket as s
HOST = '127.0.0.1'
PORT = 3000
sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()
sck.accept()