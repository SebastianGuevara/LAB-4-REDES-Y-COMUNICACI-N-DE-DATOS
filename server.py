import socket

port = 15200
server = socket.gethostbyname(socket.gethostname())
address = (server, port)
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(address)
print("El servidor esta listo para recibir")

while True:
    data, clientAddress = serverSocket.recvfrom(4096)
    print(data.decode('utf-8'))
    msg = bytes("[SERVIDOR] "+data.decode('utf-8'),encoding='utf-8')
    serverSocket.sendto(msg,clientAddress)

# format = 'utf-8'

# socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socketServer.bind(address)

# def handle_client(conn,addr):
#     print(f"[NUEVA CONEXIÓN] {addr} conextado.")

#     connected = True;
#     while connected:
#         msg_lenght = conn.recv(header).decode(format)
#         msg_lenght = int(msg_lenght)
#         msg = conn.recv(msg_lenght).decode(format)
#         print(f"[{addr}] {msg}")

# def start():
#     socketServer.listen()
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn,addr))
#         thread.start()
#         print(f"[CONEXIONES ACTIVAS] {threading.activeCount() - 1}")

# print("[INCIANDO] el servidor esta iniciando")
# start()
