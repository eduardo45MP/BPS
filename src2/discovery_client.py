import socket

def main():
    host = "127.0.0.1"  # Endereço IP do servidor
    port = 9999

    # Criação do socket do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Envia uma mensagem para o servidor
    message = "Olá, servidor!"
    client.send(message.encode("utf-8"))

    # Fecha a conexão com o servidor
    client.close()

if __name__ == "__main__":
    main()
