import socket
import threading

import socket

def handle_client(client_socket):
    print("[*] Conexão recebida de:", client_socket.getpeername())
    
    # Recebe a mensagem do cliente
    client_message = client_socket.recv(1024).decode("utf-8")
    print("[*] Mensagem recebida do cliente:", client_message)
    
    # Responde ao cliente com uma mensagem de confirmação
    server_response = "Mensagem recebida com sucesso!"
    client_socket.send(server_response.encode("utf-8"))
    
    client_socket.close()

def start_server():
    host = "0.0.0.0"
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()


def connect_to_peer(peer_host, peer_port):
    # Lógica para se conectar a um par específico
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((peer_host, peer_port))
    # Lógica para trocar dados com o par conectado
    client.close()

# Iniciar servidor em uma thread separada
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Exemplo de como conectar-se a outro par
# Você pode expandir isso para permitir que o usuário insira o endereço do par
peer_host = "127.0.0.1"
peer_port = 9999
connect_to_peer(peer_host, peer_port)
