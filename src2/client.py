import socket

def client_request(ip, port):
    # Criando um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectando ao servidor
        client_socket.connect((ip, port))
        print("Conexão estabelecida com o servidor.")

        # Enviando a solicitação do arquivo
        client_socket.send("ips.txt".encode())

        # Recebendo os dados do arquivo do servidor
        file_data = client_socket.recv(1024).decode()
        print("Conteúdo do arquivo ips.txt:")
        print(file_data)
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")

    # Fechando o socket do cliente
    client_socket.close()

# Função principal para executar o cliente
if __name__ == "__main__":
    server_ip = input("Insira o ip de um nó: ")  # IP do servidor
    server_port = 12345       # Porta do servidor
    client_request(server_ip, server_port)
