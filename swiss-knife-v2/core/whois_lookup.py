
import socket

def whois_lookup(domain):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.verisign-grs.com", 43))
        s.send((domain + "\r\n").encode())
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
        s.close()
        print("[+] WHOIS Lookup Done")
        return response.decode(errors='ignore')
    except Exception as e:
        print(f"[-] WHOIS Error: {e}")
        return ""
