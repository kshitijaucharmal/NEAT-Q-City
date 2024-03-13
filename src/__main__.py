from neat.genome import Genome
from neat.geneh import GeneHistory
import random

gh = GeneHistory(4, 2)

ins = [(random.random()) for _ in range(gh.n_inputs)]
targets = [(0.0 if (random.random() < 0.5) else 1.0) for _ in range(gh.n_outputs)]

g = Genome(gh)
for i in range(100):
    g.mutate()


print(g)
print("Inputs: ", end=f"{ins}\n")
print()
g.backpropagate(ins, targets)
