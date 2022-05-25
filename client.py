import socket
from xmlrpc.client import ServerProxy

serverName = socket.gethostbyname(socket.gethostname())
port = 15200


clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input('Ingrese texto: ')
finalMessage = f"[{socket.gethostname()}] {message}"
clientSocket.sendto(finalMessage.encode(),(serverName,port))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()