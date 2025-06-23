import socket

def banner_grabber(ip, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        print(f"🤖 Knocking on {ip}:{port}...")

        s.connect((ip, port))

        # Send a fake HTTP GET request
        http_request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
        s.send(http_request.encode())

        banner = s.recv(2048)
        print(f"📢 Banner says:\n{banner.decode(errors='ignore')}")
        s.close()

    except Exception as e:
        print(f"❌ Error connecting to {ip}:{port} - {e}")

# Now try with Apache on localhost
# banner_grabber("192.168.41", 80)
banner_grabber("172.217.170.206", 80)
