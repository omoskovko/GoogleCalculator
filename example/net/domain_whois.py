import whois


def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


domain_name = "google.com"
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print(f"Domain registrar: {whois_info.registrar}")
    print(f"WHOIS server: {whois_info.whois_server}")
    print(whois_info)
