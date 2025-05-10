
import argparse
import json
from core import dns_recon, subdomain, portscan, waf_detect, whois_lookup, word_scraper

def main():
    parser = argparse.ArgumentParser(description="Swiss-Knife v2 - All-in-One Recon Toolkit")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("-w", "--wordlist", help="Path to subdomain wordlist")
    parser.add_argument("-t", "--target", help="Target URL for wordlist scraping")
    parser.add_argument("-o", "--output", help="Output file (JSON)")
    args = parser.parse_args()

    results = {}

    # DNS Recon
    results['dns'] = dns_recon.dns_recon(args.domain)

    # WHOIS Lookup
    results['whois'] = whois_lookup.whois_lookup(args.domain)

    # Subdomain Enumeration
    if args.wordlist:
        with open(args.wordlist, 'r') as f:
            words = f.readlines()
            results['subdomains'] = subdomain.subdomain_enum(args.domain, words)

    # Port Scanning
    results['ports'] = portscan.scan_ports(args.domain)

    # WAF Detection
    results['waf'] = waf_detect.detect_waf(args.domain)

    # Wordlist Generation
    if args.target:
        results['words'] = word_scraper.generate_wordlist(args.target)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"[+] Results saved to {args.output}")

if __name__ == "__main__":
    main()
