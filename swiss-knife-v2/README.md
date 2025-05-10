
# 🧰 Swiss-Knife v2 - Advanced Reconnaissance Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Swiss-Knife v2 is an advanced, all-in-one information gathering toolkit built in Python. It integrates DNS reconnaissance, subdomain enumeration, WHOIS lookup, port scanning, WAF detection, and wordlist generation.

---

## 🔧 Features

- DNS Records Retrieval (A, AAAA, MX, NS, SOA)
- WHOIS Lookup
- Subdomain Brute-forcing
- Port Scanner (Top ports)
- WAF Detection (Basic)
- Wordlist Generator from Web Content
- JSON Output Support

---

## 📦 Installation

```bash
git clone https://github.com/mehmeterenalpan/swiss-knife-v2/swiss-knife-v2.git
cd swiss-knife-v2
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 swiss_knife.py -d example.com -w wordlist.txt -t https://example.com -o results.json
```

### Arguments

- `-d, --domain`    : Target domain (required)
- `-w, --wordlist`  : Wordlist for subdomain discovery
- `-t, --target`    : Target URL to scrape for wordlist
- `-o, --output`    : Save results to JSON file

---

## 📸 Sample Output

```
[+] DNS Recon for: example.com
[A] ['93.184.216.34']
[+] WHOIS Lookup Done
[+] Subdomain Enumeration on: example.com
[FOUND] http://admin.example.com
[+] Scanning ports on: example.com
[OPEN] 80
[+] WAF Detected: cloudflare
```

---

## 📤 Export Options

Output is saved as structured JSON:
```json
{
  "dns": {"A": ["93.184.216.34"], "MX": []},
  "whois": "...",
  "subdomains": ["admin.example.com"],
  "ports": [80],
  "waf": "cloudflare",
  "words": ["login", "admin", "portal"]
}
```

---

## ⚠️ Legal Disclaimer

This tool is for **authorized security testing only**. Do not use on unauthorized systems. You are responsible for your actions.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
