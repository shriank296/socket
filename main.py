import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("127.0.0.1", 8000)
server_socket.bind(address)

server_socket.listen() # Listen for incoming connections
try:
    connection, client_address = server_socket.accept() # Accept a connection from a client
    print(f"I have got a connection from {client_address}")

    buffer = b''
    while buffer[-2:] != b'\r\n': # Read data until the end of the HTTP request
        data = connection.recv(2)
        if not data:
            break
        print(f"I have received data: {data}")
        buffer += data
    print(f"I have received full data {buffer}")
    connection.sendall(buffer)
finally:
    server_socket.close() # Close the server socket
    