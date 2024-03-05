import socket
from net_scan import scan_local_network

def start_server():
    host = "0.0.0.0"  # Escuta em todas as interfaces de rede
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Servidor P2P iniciado em:", host, "na porta:", port)

    return server

def check_other_servers():
    other_servers = scan_local_network()
    if other_servers:
        print("[*] Outros servidores ativos encontrados na rede. Não é o primeiro servidor.")
    else:
        print("[*] Nenhum outro servidor ativo na rede. Este é o primeiro servidor.")


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
