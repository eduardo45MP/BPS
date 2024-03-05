import nmap

def scan_local_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='10.0.0.0/24', arguments='-p 9999')  # Substitua '10.0.0.0/24' pela sua rede local
    hosts = []
    for host in nm.all_hosts():
        if nm[host]['tcp'][9999]['state'] == 'open':
            print(f"Node found at {host}:9999")
            hosts.append(host)
    return hosts
