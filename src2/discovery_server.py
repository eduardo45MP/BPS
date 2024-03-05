# discovery_server.py
import json
import socket
import threading

class DiscoveryServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.nodes = set()  # Conjunto para armazenar os nós ativos
        self.server = None

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        print(f"Discovery server started on {self.host}:{self.port}")

        while True:
            client_socket, _ = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        # Adiciona o endereço do nó à lista de nós ativos
        node_address = client_socket.recv(1024).decode()
        self.nodes.add(node_address)
        print(f"Node {node_address} connected.")

        # Envie a lista de outros nós ativos para o novo nó
        client_socket.send(json.dumps(list(self.nodes)).encode())

    def get_active_nodes(self):
        return list(self.nodes)

if __name__ == "__main__":
    discovery_server = DiscoveryServer("localhost", 5001)
  
