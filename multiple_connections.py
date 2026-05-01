import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
socket_server.bind(server_address)
socket_server.listen()

connections = []

try:
    while True:
        connection, client_address = socket_server.accept()
        print(f"I received a connection from {client_address}")
        connections.append(connection)

        for connection in connections:
            buffer = b""
            while buffer[-2:] != b"\r\n":
                data = connection.recv(2)
                if not data:
                    break
                print(f"I have got data: {data}")
                buffer = buffer + data
            print(f"All data is: {buffer}")
            connection.sendall(buffer)
finally:
    socket_server.close()




