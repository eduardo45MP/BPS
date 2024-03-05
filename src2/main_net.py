import socket
import json
import threading
from node import Node
from discovery_server import DiscoveryServer

def check_existing_nodes(discovery_server_host, discovery_server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((discovery_server_host, discovery_server_port))
            client_socket.send(b"GET_ACTIVE_NODES")
            nodes_data = client_socket.recv(1024).decode()
            return json.loads(nodes_data)
    except ConnectionRefusedError:
        return []

def main():
    discovery_server_host = "localhost"
    discovery_server_port = 5001
    node_host = "localhost"
    node_port = 5000

    existing_nodes = check_existing_nodes(discovery_server_host, discovery_server_port)

    if existing_nodes:
        print("Existing nodes found in the network:")
        for node_address in existing_nodes:
            print(node_address)

        # Choose one of the existing nodes to connect
        peer_host, peer_port = existing_nodes[0].split(":")
        peer_port = int(peer_port)

        # Connect to an existing node
        node = Node(node_host, node_port, discovery_server_host, discovery_server_port)
        node.connect_to_peer(peer_host, peer_port)
    else:
        print("No existing nodes found. Starting a new network.")

        # Start the discovery server
        discovery_server = DiscoveryServer(discovery_server_host, discovery_server_port)
        discovery_server_thread = threading.Thread(target=discovery_server.start)
        discovery_server_thread.daemon = True
        discovery_server_thread.start()

        # Start the node
        node = Node(node_host, node_port, discovery_server_host, discovery_server_port)
        node.start()

if __name__ == "__main__":
    main()
