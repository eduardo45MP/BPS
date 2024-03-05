import socket
from net_scan import scan_local_network

def main():
    # Lista de endereços IP e portas dos nós da rede local
    nodes = scan_local_network()

    # Criação do socket do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for node in nodes:
        try:
            # Conecta-se a cada nó na lista
            client.connect(node)

            # Envia uma mensagem para o nó
            message = "Olá, nó!"
            client.send(message.encode("utf-8"))

            # Fecha a conexão com o nó
            client.close()
        except Exception as e:
            print("Erro ao conectar-se ao nó:", e)

if __name__ == "__main__":
    main()
