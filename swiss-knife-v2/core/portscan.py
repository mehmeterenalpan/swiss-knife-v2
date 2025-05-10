
import socket

def scan_ports(host, ports=[21,22,23,25,53,80,110,139,143,443,445,3389]):
    print(f"[+] Scanning ports on: {host}")
    open_ports = []
    for port in ports:
        try:
            sock = socket.create_connection((host, port), timeout=1)
            print(f"[OPEN] {port}")
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports
