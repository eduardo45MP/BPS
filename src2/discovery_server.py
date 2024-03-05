import socket
import threading

# Função para lidar com a conexão de novos pares
def handle_client(client_socket):
    print("[*] Conexão recebida de:", client_socket.getpeername())
    # Lógica para lidar com a comunicação com o par conectado
    # Aqui você pode implementar o protocolo de troca de dados P2P
    client_socket.close()

def start_server():
    # Configuração do servidor
    host = "0.0.0.0"  # Todas as interfaces de rede
    port = 9999  # Porta para ouvir conexões

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    # Loop para aceitar conexões de novos pares
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

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
