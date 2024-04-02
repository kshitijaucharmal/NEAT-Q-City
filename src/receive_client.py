# TESTING FOR THE SOCKET

import socket

# Server host and ports
HOST = "localhost"
ports = range(40000, 40016)

def test_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        while True:
            # Receive data from the server
            data = s.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            # Send "next" to request more data
            s.sendall(b"next")
        # Send "exit" to terminate the connection
        s.sendall(b"exit")

# Test the server on each port
for port in ports:
    print(f"Testing server on port {port}")
    test_server(port)
    print("Test completed.")
