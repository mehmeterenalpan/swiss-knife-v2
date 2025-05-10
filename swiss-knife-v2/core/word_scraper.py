
import requests
from bs4 import BeautifulSoup

def generate_wordlist(target_url):
    print(f"[+] Generating Wordlist from: {target_url}")
    words = set()
    try:
        r = requests.get(target_url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        for text in soup.stripped_strings:
            for word in text.split():
                word = word.lower()
                if len(word) > 4:
                    words.add(word)
        print(f"[+] Words Collected: {len(words)}")
    except Exception as e:
        print(f"[-] Error: {e}")
    return sorted(words)
