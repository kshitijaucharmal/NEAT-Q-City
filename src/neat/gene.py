import random
import pygame

class Gene:
    # here gene refers to CONNECTION between two nodes (in_node and out_node)
    def __init__(self, i, o):
        # in_node and out_node are node objects which are having connection in between
        self.in_node = i
        self.out_node = o
        # gene weight
        self.weight = random.random() * 4 - 2  # (-2,2)
        # innovation ID
        self.inno = -1
        self.enabled = True
        self.error=0
        # For showing
        self.color = (0, 255, 0)
        pass

    # Clone the gene
    def clone(self):
        g = Gene(self.in_node.clone(), self.out_node.clone())
        g.weight = self.weight
        g.enabled = self.enabled
        g.inno = self.inno
        return g
    
    # Simple mutations to weight
    def mutate(self):
        if random.random() < 0.1:
            self.weight = random.random() * 4 - 2
        else:
            self.weight += random.uniform(-0.2, 0.2)
            # Clamping
            self.weight = self.weight if self.weight < 2 else 2
            self.weight = self.weight if self.weight > -2 else -2

    # Get Some info
    def get_info(self):
        s = str(self.inno) + "] "
        s += str(self.in_node.number) + "(" + str(self.in_node.layer) + ") -> "
        s += str(self.out_node.number) + "(" + str(self.out_node.layer) + ") "
        s += str(self.weight) + " "
        s += str(self.enabled) + '\n'
        return s    
    # s = 3] 2(1) -> 4(2) -1.534534 TRUE
    # innovation_no] in_node_number(in_node_layer) -> out_node_number(out_node_layer) Weight Enabled

    #helper function to convert object into string
    def __str__(self) -> str:
        return self.get_info()

    # For displaying
    def show(self, ds):
        # red if weight > 0 and blue if weight<0
        self.color = (255, 0, 0) if self.weight > 0 else (0, 0, 255)
        # GREEN if connection(gene) is disabled
        if not self.enabled:
            self.color = (0, 255, 0)
        pygame.draw.line(ds, self.color, self.in_node.pos, self.out_node.pos, 3) # last parameter is thickness
        pass
