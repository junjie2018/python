import dns.resolver

res = dns.resolver.query('dnspython.org', 'NS')
for item in res.response.answer:
    print(item)

res = dns.resolver.query('dnspython.org', 'A')
for item in res.response.answer:
    print(item)