run = True
import socket as s
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
class InitComms:
    def __init__(self):
        print(f"IP to connect is {s.gethostbyname(s.gethostname())}")
    class  client:
        def __init__(self, ip):
            self.ip = ip
            sock.connect((self.ip, 80))

        def sendMsg(self, message):
            self.message = message
            sock.send(bytes(str(message), 'utf-8'))

        def recieve(self):
            self.recvMsg = sock.recv(1024).decode('utf-8')
            print(self.recvMsg)

    class server:
        def __init__(self, queue=1):
            sock.bind(("", 80))
            sock.listen(queue)
        while True:
            self.client, self.addr = sock.accept()
            if self.addr != "":
                break

        def sendMsg(self, message):
            self.message = message
            self.client.send(bytes(str(self.message), 'utf-8'))
        def recieve(self):
            recvMsg = self.client.recv(1024).decode('utf-8')
            print(recvMsg)
            run = False
            while run is True:
                self.client, self.addr = sock.accept()
                if addr != "":
                    run = False
