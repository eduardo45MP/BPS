import socket
import uuid

def get_ipv4_address():
    try:
        # Criando um socket para obter o endereço IP local
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_socket:
            temp_socket.connect(("8.8.8.8", 80))
            own_ip = temp_socket.getsockname()[0]
        return own_ip
    except Exception as e:
        print(f"Erro ao obter o endereço IPv4 do servidor: {e}")
        return None

def send_ips_file(client_socket):
    try:
        # Lendo o conteúdo do arquivo ips.txt
        with open("ips.txt", "r") as file:
            file_content = file.read()
            # Enviando o conteúdo do arquivo para o cliente
            client_socket.send(file_content.encode())
        print("Arquivo ips.txt enviado para o cliente.")
    except FileNotFoundError:
        print("Arquivo ips.txt não encontrado.")

def create_server():
    # Obtendo o endereço IPv4 do servidor
    own_ip = get_ipv4_address()

    if own_ip is None:
        print("Não foi possível obter o endereço IPv4 do servidor. Encerrando...")
        return

    # Configurações do servidor
    host = own_ip       # Endereço IP do servidor
    port = 12345        # Porta que o servidor irá escutar

    # Criando um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ligando o socket ao endereço e porta especificados
    server_socket.bind((host, port))

    # Habilitando o servidor para aceitar conexões
    server_socket.listen(1)
    print("Servidor está ouvindo...")

    while True:
        # Aceitando a conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")

        # Enviando o arquivo ips.txt para o cliente
        send_ips_file(client_socket)

        # Fechando a conexão com o cliente
        client_socket.close()

# Função principal para executar o servidor
if __name__ == "__main__":
    create_server()
