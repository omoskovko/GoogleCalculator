import dns.resolver

target_domain = "thepythoncode.com"
# see all the available DNS records and their functions at
# https://en.wikipedia.org/wiki/List_of_DNS_record_types
records_type = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
resolver = dns.resolver.Resolver()
for record in records_type:
    try:
        answers = resolver.resolve(target_domain, record)
    except dns.resolver.NoAnswer:
        continue

    print(f"DNS records for {target_domain} ({record}):")
    for data in answers:
        print(data)
