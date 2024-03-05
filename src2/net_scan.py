import socket
import ipaddress

def scan_local_network():
    subnet = '10.0.0.0/24'  # Substitua pelo seu intervalo de rede local
    hosts = []

    # Itera sobre todos os endereços IP na sub-rede
    for ip in ipaddress.IPv4Network(subnet):
        host = str(ip)
        try:
            # Tenta conectar à porta 9999
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  # Define um tempo limite curto para a conexão
                s.connect((host, 9999))
                print(f"Node found at {host}:9999")
                hosts.append(host)
        except (socket.timeout, ConnectionRefusedError):
            pass  # Ignora se a conexão falhar ou se o tempo limite for atingido

    return hosts