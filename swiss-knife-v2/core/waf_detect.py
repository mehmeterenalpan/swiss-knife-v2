
import requests

def detect_waf(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        headers = response.headers
        wafs = ["cloudflare", "sucuri", "imperva", "akamai"]
        for h in headers.values():
            for waf in wafs:
                if waf in h.lower():
                    print(f"[+] WAF Detected: {waf}")
                    return waf
    except:
        pass
    return "None"
