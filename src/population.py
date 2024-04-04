import socket
import random

from city import City
from neat.geneh import GeneHistory

HOST = "localhost"
PORT = 50000

msg = ""


class Population:
    def __init__(self, pop_size=16):
        self.pop_size = pop_size
        self.population = []
        self.n_states = 10
        self.n_actions = 10
        self.gene_history = GeneHistory(10, 10)
        for _ in range(pop_size):
            self.population.append(City(self.gene_history))
            self.population[-1].calculate_fitness()

        self.generation = 1
        self.best_fitness = 0
        self.reset()
        pass

    def update(self, conn):
        msg = ""
        for p in self.population:
            action = p.train()
            # Add to message
            s = p.city_details(action)
            msg += s + ":"

        # Remove the last :
        msg = msg[:-1]
        print(msg)

        # Send it
        conn.sendall(str(msg).encode())
        # Check if recieved
        cmd = conn.recv(1024).decode()
        return cmd

    def reset(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)

        for i in range(self.pop_size):
            parent1 = self.population[random.randint(0, 4)]
            parent2 = self.population[random.randint(0, 4)]

            # Perform crossover
            child = parent1.crossover(parent2)
            # Mutate it some
            child.mutate()
            # Set child to population
            self.population[i] = child

    def start_server(self):
        # start server (socket)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set socket options
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        print(f"{PORT} listening...")

        s.listen()
        conn, addr = s.accept()
        print(f"Connected to {addr}")

        while True:
            cmd = self.update(conn)

            if "reset" in cmd:
                print("Updated Generation")
                self.reset()
                continue

            if "exit" in cmd:
                break
            if "next" in cmd:
                continue

        s.close()


pop = Population(16)
pop.start_server()
