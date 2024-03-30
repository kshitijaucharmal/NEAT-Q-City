import numpy as np
import socket

HOST = "localhost"
port = 65432

msg = ""


def open_port(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # start server
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, p))
    print(f"{port} bound")

    s.listen()
    conn, addr = s.accept()

    print(f"Connected to {addr}")

    while True:
        msg = f"Random number is: {np.random.random()}"
        conn.sendall(str(msg).encode())
        cmd = conn.recv(1024).decode()
        if "next" in cmd:
            continue

        if "exit" in cmd:
            break


open_port(port)
