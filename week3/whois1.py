import whois 

domain = whois.whois('https://www.scrapethissite.com/')


print("Domain Name:", domain.domain_name)
print("Registrar:", domain.registrar)
print("Creation Date:", domain.creation_date)
print("Expiration Date:", domain.expiration_date)
print("Name Servers:", domain.name_servers)