from neat.genome import Genome
from neat.geneh import GeneHistory
from stats_socket_send import open_port
from receive_client import run_client

gh = GeneHistory(4, 2)

g = Genome(gh)
for i in range(100):
    g.mutate()


# print(g)
# print("Inputs: ", end=f"{ins}\n")
# print()
# g.backpropagate(ins, targets)
