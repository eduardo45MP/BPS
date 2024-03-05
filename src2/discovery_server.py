import socket

def start_server():
    host = "0.0.0.0"  # Escuta em todas as interfaces de rede
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    return server

def check_other_servers():
    other_servers = ["10.0.0.1", "10.0.0.2"]  # Exemplo de outros servidores conhecidos na rede
    for server_ip in other_servers:
        try:
            # Tenta conectar-se a outro servidor
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Define um tempo limite curto para a conexão
                s.connect((server_ip, 9999))
                print("[*] Servidor encontrado em:", server_ip)
                return True
        except (socket.timeout, ConnectionRefusedError):
            pass  # Ignora se a conexão falhar ou se o tempo limite for atingido

    print("[*] Nenhum outro servidor encontrado na rede")
    return False

def main():
    # Verifica se há outros servidores ativos na rede
    if not check_other_servers():
        print("[*] Nenhum outro servidor ativo na rede. Este é o primeiro servidor.")
    else:
        print("[*] Outros servidores ativos encontrados na rede. Não é o primeiro servidor.")

    server = start_server()

    while True:
        client_socket, addr = server.accept()
        print("[*] Conexão recebida de:", addr)

        # Lógica para lidar com a conexão do cliente aqui

        client_socket.close()

if __name__ == "__main__":
    main()
