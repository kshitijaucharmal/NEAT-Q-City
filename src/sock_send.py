import numpy as np
import socket
import threading

HOST = "localhost"

msg = ""
n_states = 10


def open_port(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # start server
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, p))
    print(f"{p} bound")

    s.listen()
    conn, addr = s.accept()

    print(f"Connected {p} to {addr}")
    allStates = [(round(np.random.random(), 4)) for _ in range(n_states)]
    allStates.append(np.random.randint(0, 10))

    while True:
        allStates[-1] = np.random.randint(0, 10)

        msg = ""
        for v in allStates:
            msg += str(v) + ","
        msg = msg[:-1]

        conn.sendall(str(msg).encode())
        cmd = conn.recv(1024).decode()

        if "next" in cmd:
            continue

        if "exit" in cmd:
            break


ports = range(4321, 4337)
threads = []
for port in ports:
    thread = threading.Thread(target=open_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
