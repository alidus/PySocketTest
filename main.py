import socket;

print("Starting")
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_socket.bind(('127.0.0.1', 53210))
serv_socket.listen(10)

print("Listening...")
client_sock, client_addr = serv_socket.accept()
#print(client_sock, client_addr)

while True:
    data = client_sock.recv(1024)
    print("Recieved: ", data)
    if not data:
        break
    client_sock.sendall(data)