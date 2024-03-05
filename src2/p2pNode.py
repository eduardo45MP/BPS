import socket
import threading

class P2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []
        self.server = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server.accept()
            print(f"Connection established with {client_address[0]}:{client_address[1]}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def connect_to_peer(self, peer_host, peer_port):
        peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer_socket.connect((peer_host, peer_port))
        self.peers.append(peer_socket)
        print(f"Connected to peer {peer_host}:{peer_port}")

    def broadcast_message(self, message):
        for peer_socket in self.peers:
            peer_socket.send(message.encode())

    def listen_for_messages(self):
        while True:
            for peer_socket in self.peers:
                message = peer_socket.recv(1024).decode()
                if message:
                    print(f"Received message from peer: {message}")
                    # Aqui você pode processar a mensagem recebida conforme necessário
                    # Por exemplo, você pode verificar se a mensagem é válida e executar ação com base nela
                    # Ou encaminhar a mensagem para outros nós na rede, se necessário

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received message from client: {message}")
                    # Aqui você pode processar a mensagem recebida do cliente e executar ação com base nela
                    # Por exemplo, você pode tratar solicitações de transações, blocos, etc.
                    # e responder de acordo com o protocolo da sua rede Blockchain
            except ConnectionResetError:
                # Se a conexão com o cliente for perdida, remova-o da lista de peers e encerre o loop
                print("Client disconnected.")
                self.peers.remove(client_socket)
                break

if __name__ == "__main__":
    node = P2PNode("localhost", 5000)
    node.start_server()
