import socket
import threading

class Node:
    def __init__(self, host, port, discovery_server_host, discovery_server_port):
        self.host = host
        self.port = port
        self.discovery_server_host = discovery_server_host
        self.discovery_server_port = discovery_server_port
        self.server = None

    def register_with_discovery_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.discovery_server_host, self.discovery_server_port))
            address = f"{self.host}:{self.port}"
            client_socket.send(address.encode())

    def start(self):
        self.register_with_discovery_server()
        self.start_server()
        print(f"Node started on {self.host}:{self.port}")

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, _ = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        # Aqui você pode adicionar a lógica para lidar com diferentes tipos de mensagens
        # Por exemplo, você pode verificar o tipo da mensagem e responder adequadamente

        client_socket.close()

    def send_message(self, peer_host, peer_port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((peer_host, peer_port))
            client_socket.send(message.encode())

if __name__ == "__main__":
    node = Node("localhost", 5000, "localhost", 5001)
    node.start()
