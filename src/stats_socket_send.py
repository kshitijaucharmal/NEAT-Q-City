import socket
import threading
import random
from stats_manager.manager import StatManager
import time

HOST = "localhost"

msg = ""
n_states = 10

ACTIONS = [
    "BuildHospital",
    "BuildPark",
    "BuildFactory",
    "BuildTransport",
    "BuildEducationInstitutes",
    "BuildResidentialBuilding",
    "BuildOffices",
    "DevelopScienceCenter",
    "BuildFarm",
    "DevelopRenewableEnergy",
]


def send_stats(conn, stats, action_number):
    msg = ",".join(str(round(v, 4)) for v in stats)
    msg += "," + str(action_number)
    conn.sendall(str(msg).encode())
    time.sleep(0.1)


def open_port(p):
    # start server (socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set socket options
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, p))
    print(f"{p} bound and listening...")

    s.listen()
    conn, addr = s.accept()

    print(f"Connected to {addr}")

    obj = StatManager()

    while True:
        action_name = random.choice(ACTIONS)
        action_number = ACTIONS.index(action_name)

        obj.take_action(action_name)

        send_stats(conn, obj.all_stats.values(), action_number)

        cmd = conn.recv(1024).decode()

        if "next" in cmd:
            continue

        if "exit" in cmd:
            break


ports = range(60000, 60016)
threads = []
for port in ports:
    thread = threading.Thread(target=open_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
