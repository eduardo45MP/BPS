import socket

def start_server():
    host = "0.0.0.0"  # Escuta em todas as interfaces de rede
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    return server

def main():
    server = start_server()

    while True:
        client_socket, addr = server.accept()
        print("[*] Conexão recebida de:", addr)

        # Lógica para lidar com a conexão do cliente aqui

        client_socket.close()

if __name__ == "__main__":
    main()
