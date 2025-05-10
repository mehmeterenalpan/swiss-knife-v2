
import threading
import requests

def subdomain_enum(domain, wordlist):
    print(f"[+] Subdomain Enumeration on: {domain}")
    found = []

    def check(sub):
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"[FOUND] {url}")
            found.append(f"{sub}.{domain}")
        except:
            pass

    threads = []
    for word in wordlist:
        t = threading.Thread(target=check, args=(word.strip(),))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return found
