import socket


class server:
    def __init__(self,array):
        self.array=array
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), 12345))
        self.s.listen(5)
    def sendmsg(self):
        while True:
            clientsocket,addr=self.s.accept()
            print(f"connection from {addr} has been accepted")
            clientsocket.send(bytes(str(self.array),"utf-8"))

