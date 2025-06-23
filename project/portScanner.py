import socket 


def scan_ports(target_ip, port_range):
     print(f"Scanning ports on {target_ip}...")

for port in  port_range:  

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  s.settimeout(1)
  result = s.connect_ex((target_ip, port))



