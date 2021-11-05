import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] New thread started for "+ip+":"+str(port))


    def run(self):    
        print ("Connection from : "+ip+":"+str(port))

        data = "emptydat"

        while len(data):
            data = clientsock.recv(1024)
            datacheck = data.decode('utf-8')
            print ("Client sent : "+datacheck)

            if datacheck.upper == 'EXIT':
                clientsock.send((data))
                break
            else:
                if not data:
                    break
                else:
                    clientsock.send((data))
        print ("Client disconnected...")

host = "0.0.0.0"
port = 8080

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print ("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
