import numpy as np
import threading
import socket

HOST = "localhost"
ports = range(65400, 65500)

msg = ""


def open_port(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # start server
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, p))
    s.listen()
    conn, addr = s.accept()

    print(f"Connected to {addr}")

    while True:
        msg = f"Hello from {p}"
        conn.sendall(str(msg).encode())
        cmd = conn.recv(1024)
        if "exit" in cmd.decode():
            break


threads = []
for p in ports:
    thread = threading.Thread(target=open_port, args=(p,))
    threads.append(thread)
    thread.start()
print("All ports bound")

for thread in threads:
    thread.join()
