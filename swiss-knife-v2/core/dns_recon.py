
import dns.resolver

def dns_recon(domain):
    print(f"[+] DNS Recon for: {domain}")
    record_types = ['A', 'AAAA', 'MX', 'NS', 'SOA']
    dns_results = {}
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            dns_results[rtype] = [str(ans) for ans in answers]
            print(f"[{rtype}] {dns_results[rtype]}")
        except:
            pass
    return dns_results
