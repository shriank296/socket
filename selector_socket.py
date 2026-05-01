import selectors
import socket
from selectors import SelectorKey
from typing import List

selector = selectors.DefaultSelector()

socket_server = socket.socket()
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
socket_server.setblocking(False)
socket_server.bind(server_address)
socket_server.listen()

selector.register(socket_server, selectors.EVENT_READ)

while True:
    events: List[tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("No events, waiting a bit more")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == socket_server:
            connection, client_address = socket_server.accept()
            connection.setblocking(False)
            print(f"I have got a connection from {client_address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"I have got some data: {data}")
            event_socket.send(data)        
