# import requests

# def is_domain_activated(domain):
#     try:
#         # Ensure the domain starts with http/https
#         if not domain.startswith(("http://", "https://")):
#             domain = "http://" + domain
        
#         # Send a request to the domain
#         response = requests.get(domain, timeout=5)
        
#         # Check if the response status is OK (200-399 range)
#         if response.status_code < 400:
#             return True
#         else:
#             return False
#     except requests.exceptions.RequestException:
#         return False

# # Example usage
# domain = "https://grc.transasiatec.com/"
# if is_domain_activated(domain):
#     print(f"The domain {domain} is activated.")
# else:
#     print(f"The domain {domain} is not activated.")


import socket

def is_domain_reachable(domain, port=80):
    try:
        socket.setdefaulttimeout(5)
        socket.create_connection((domain, port))
        return True
    except (socket.timeout, socket.error):
        return False

# Example usage
domain = "transdedu.transasiatec.com"
if is_domain_reachable(domain):
    print(f"The domain {domain} is reachable.")
else:
    print(f"The domain {domain} is not reachable.")
