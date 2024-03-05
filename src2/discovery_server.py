import socket

def main():
    host = "0.0.0.0"  # O servidor aceitará conexões de qualquer interface de rede
    port = 9999

    # Criação do socket do servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    # Loop principal para aceitar conexões
    while True:
        client_socket, addr = server.accept()
        print("[*] Conexão recebida de:", addr)

        # Recebe mensagem do cliente
        client_message = client_socket.recv(1024).decode("utf-8")
        print("[*] Mensagem recebida do cliente:", client_message)

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    main()
