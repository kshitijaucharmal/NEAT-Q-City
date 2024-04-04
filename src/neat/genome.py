from neat.node import Node
from neat.gene import Gene

import random
import numpy as np
import math

# genome represents an individual neural network architecture
class Genome:
    
    def __init__(self, gh):
        # Ref to gene history(gh)
        self.gh = gh
        # Copying inputs/outputs
        self.n_inputs = gh.n_inputs
        self.n_outputs = gh.n_outputs
        # Total Nodes (used as ctr)
        self.total_nodes = 0

        # Nodes and genes
        self.nodes = []
        self.genes = []

        #batch size 
        self.batch_size = 32 # update the same value in a agent file (line no 17)

        # Random fitness for now
        self.fitness = random.uniform(-2, 2)
        self.adjusted_fitness = 0

        # Input nodes
        for _ in range(self.n_inputs):
            self.nodes.append(Node(self.total_nodes, 0))
            self.total_nodes += 1

        # output nodes
        for _ in range(self.n_outputs):
            self.nodes.append(Node(self.total_nodes, 1))
            self.total_nodes += 1
        pass

    def clone(self):
        clone = Genome(self.gh)
        clone.total_nodes = self.total_nodes
        clone.nodes.clear()
        clone.genes.clear()

        for i in range(len(self.nodes)):
            clone.nodes.append(self.nodes[i].clone())

        for i in range(len(self.genes)):
            clone.genes.append(self.genes[i].clone())

        clone.connect_genes()
        return clone

    # Gene with inno exists
    def exists(self, inno):
        for g in self.genes:
            if g.inno == inno:
                return True
        return False

    # Connect nodes
    def connect_nodes(self, n1, n2):
        n1layer = n1.layer if n1.layer != 1 else 1000000
        n2layer = n2.layer if n2.layer != 1 else 1000000

        if n1layer > n2layer:
            n1, n2 = n2, n1

        c = self.gh.exists(n1, n2)
        x = Gene(n1, n2)

        if c:
            x.inno = c.inno
            if not self.exists(x.inno):
                self.genes.append(x)
        else:
            x.inno = self.gh.global_inno
            self.gh.global_inno += 1
            self.gh.all_genes.append(x.clone())
            self.genes.append(x)
        pass

    # Mutate add gene
    def add_gene(self):
        n1 = random.choice(self.nodes)
        n2 = random.choice(self.nodes)

        while n1.layer == n2.layer:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)

        self.connect_nodes(n1, n2)
        pass

    # Random Mutations
    def mutate(self):
        if len(self.genes) == 0:
            self.add_gene()

        if random.random() < 0.8:
            for i in range(len(self.genes)):
                self.genes[i].mutate()
        if random.random() < 0.08:
            self.add_gene()
        if random.random() < 0.02:
            self.add_node()
        pass

    def get_node(self, n):
        for i in range(len(self.nodes)):
            if self.nodes[i].number == n:
                return self.nodes[i]
        print("Node not found : Something's Wrong")
        return None

    # Connect genes to get ready for output calculation
    def connect_genes(self):
        for i in range(len(self.genes)):
            self.genes[i].in_node = self.get_node(self.genes[i].in_node.number)
            self.genes[i].out_node = self.get_node(self.genes[i].out_node.number)

        for i in range(len(self.nodes)):
            self.nodes[i].in_genes.clear()

        # Add in_genes
        for i in range(len(self.genes)):
            self.genes[i].out_node.in_genes.append(self.genes[i])
        pass
    
    def seperate(self):
        # Seperating the nodes layer-wise
        self.Input_Layer=[]
        self.Output_Layer=[]
        self.HL_1=[]
        self.HL_2=[]

        for i in range(len(self.nodes)):
            if(self.nodes[i].layer == 0):
                self.Input_Layer.append(self.nodes[i])
            elif self.nodes[i].layer == 1:
                self.Output_Layer.append(self.nodes[i])
            elif self.nodes[i].layer == 2:
                self.HL_1.append(self.nodes[i])
            elif self.nodes[i].layer == 3:
                self.HL_2.append(self.nodes[i])
            else:
                print("Something is wrong while seperating nodes")
        pass

    # Forward Propogation
    def feed_forward(self, inputs):
        #print(f"inputs inside feedforward:",inputs)
        final_outputs = np.zeros((self.batch_size, self.n_outputs))
        for i in range(len(inputs)):
            #print(f"feed inputs: ",inputs[i])
            #print(f"feed n_inputs: ",self.n_inputs)
            if len(inputs[i]) != self.n_inputs:
                print("Wrong number of inputs")
                return [-1]

            # Input layers outputs are the specified inputs
            for j in range(self.n_inputs):
                self.nodes[j].sum=inputs[i][j]
                self.nodes[j].output = inputs[i][j]

            # Connect genes (Clean references)
            self.connect_genes()

            # calculate layer wise
            for layer in range(2, self.gh.highest_hidden + 1):
                nodes_in_layer = []
                for n in range(len(self.nodes)):
                    if self.nodes[n].layer == layer:
                        nodes_in_layer.append(self.nodes[n])

                for n in range(len(nodes_in_layer)):
                    nodes_in_layer[n].calculate()

            # calculate final outputs at last
            #final_outputs = np.zeros((self.batch_size, self.n_outputs))
            j=0
            for n in range(self.n_inputs, self.n_inputs + self.n_outputs):
                self.nodes[n].calculate()
                #print(f"node",self.nodes[n].output)
                final_outputs[i][j]=(self.nodes[n].output)
                j+=1
        #print(f" feed final_outputs:",final_outputs)
            
        # return outputs
        return final_outputs

    # ---------------------------------Backpropogation-------------------------------------------
    def mean_squared_error(self,target, pred):
        # print(f"Target:",target)
        # print(f"Pred:",pred)
        if len(target)!=len(pred):
            print("Unequal length of inputs and outputs")

        self.squared_difference = [(target[i]-pred[i])**2 for i in range(len(pred))]
        # print(f"squared:",self.squared_difference)
        return np.mean(self.squared_difference)

    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_derivative(self,x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))
    

    def backpropogate(self,inputs,targets):
        #print(f"back inputs:",inputs)
        #print(f"back targets:",targets)
        #learning_rate
        self.lr=0.001
        #calling seprate function to get the layerwise list
        self.seperate()
        
            # generating the outputs
        self.predicted_output=self.feed_forward(inputs)
        #print("back predicted_output:",self.predicted_output)



        for k in range(len(inputs)): # loop for batched inputs

            for i in range(len(self.nodes)):
                self.nodes[i].value=0
            # Backpropagation
            # Compute gradients of loss with respect to output layer
            self.d_loss_output = [(targets[k][i] - self.predicted_output[k][i]) for i in range(len(targets[0]))]
            self.d_output_input3 = [self.d_loss_output[i] * self.sigmoid_derivative(self.Output_Layer[i].sum) for i in range(len(targets[0]))]
            for i in range(len(self.Output_Layer)):
                for j in range(len(self.Output_Layer[i].in_genes)):
                    self.temp_gene=self.Output_Layer[i].in_genes[j]
                    if(self.temp_gene.enabled==True):
                        self.temp_gene.error = self.d_output_input3[i] * self.temp_gene.in_node.output
                        # updating weights
                        self.temp_gene.weight+=(self.lr*self.temp_gene.error)
                        #print(f"updating weights..")
                        # storing the required value in node
                        self.temp_gene.in_node.value += (self.d_output_input3[i] * self.temp_gene.weight)
                        #print(f"updating value in nodes..")

            # Compute gradients of loss with respect to second hidden layer
            self.d_output_input2 = [self.HL_2[i].value * self.sigmoid_derivative(self.HL_2[i].sum) for i in range(len(self.HL_2))]
            for i in range(len(self.HL_2)):
                for j in range(len(self.HL_2[i].in_genes)):
                    self.temp_gene=self.HL_2[i].in_genes[j]
                    if(self.temp_gene.enabled==True):
                        self.temp_gene.error = self.d_output_input2[i] * self.temp_gene.in_node.output
                        # updating weights
                        self.temp_gene.weight+=(self.lr*self.temp_gene.error)
                        #print(f"updating weights..")
                        # storing the required value in node
                        self.temp_gene.in_node.value += (self.d_output_input2[i] * self.temp_gene.weight)
                        #print(f"updating value in nodes..")

            # Compute gradients of loss with respect to first hidden layer
            self.d_output_input1 = [self.HL_1[i].value * self.sigmoid_derivative(self.HL_1[i].sum) for i in range(len(self.HL_1))]
            for i in range(len(self.HL_1)):
                for j in range(len(self.HL_1[i].in_genes)):
                    self.temp_gene=self.HL_1[i].in_genes[j]
                    if(self.temp_gene.enabled==True):
                        self.temp_gene.error = self.d_output_input1[i] * self.temp_gene.in_node.output
                        # updating weights
                        self.temp_gene.weight+=(self.lr*self.temp_gene.error)
                        #print(f"updating weights..")
                        # storing the required value in node
                        self.temp_gene.in_node.value += (self.d_output_input1[i] * self.temp_gene.weight)
                        #print(f"updating value in nodes..")

        #print(f"mse:",self.mean_squared_error(targets,self.feed_forward(inputs)))
        pass
    
    # get weight of gene of inno
    def get_weight(self, inno):
        for g in self.genes:
            if g.inno == inno:
                return g.weight
        return -1

    # Compatibility calculation
    def calculate_compatibility(self, partner):
        try:
            p1_highest_inno = max([(a.inno) for a in self.genes])
        except Exception:
            p1_highest_inno = 0

        try:
            p2_highest_inno = max([(a.inno) for a in partner.genes])
        except Exception:
            p2_highest_inno = 0

        # Set highest inno (Should be one with highest fitness)
        highest_inno = max(p1_highest_inno, p2_highest_inno)

        matching = 0
        disjoint = 0
        excess = 0

        c1 = 1.0
        c2 = 1.0
        c3 = 0.4

        flag = 0

        total_weights = 0

        for i in range(highest_inno):
            e1 = self.exists(i)
            e2 = partner.exists(i)
            if e1 and e2:
                matching += 1
                flag = i
                total_weights += self.get_weight(i) - partner.get_weight(i)
                continue

        disjoint = (flag + 1) - matching
        excess = highest_inno - flag

        if matching == 0:
            matching = 1
        avg_weights = total_weights / matching

        N = 1 if highest_inno < 20 else highest_inno
        excess_coeff = c1 * excess / N
        disjoint_coeff = c2 * disjoint / N
        weight_coeff = c3 * avg_weights

        # Compatibility distance
        cd = excess_coeff + disjoint_coeff + weight_coeff

        # print(matching, disjoint, excess)
        # print("Compatibility Distance", cd)
        return cd

    # Mutate add node
    def add_node(self):
        if len(self.genes) == 0:
            self.add_gene()

        if random.random() < 0.2:
            self.gh.highest_hidden += 1

        n = Node(self.total_nodes, random.randint(2, self.gh.highest_hidden))
        self.total_nodes += 1

        g = random.choice(self.genes)
        l1 = g.in_node.layer
        l2 = g.out_node.layer
        if l2 == 1:
            l2 = 1000000

        while l1 > n.layer or l2 < n.layer:
            g = random.choice(self.genes)
            l1 = g.in_node.layer
            l2 = g.out_node.layer
            if l2 == 1:
                l2 = 1000000

        self.connect_nodes(g.in_node, n)
        self.connect_nodes(n, g.out_node)
        self.genes[-1].weight = 1.0
        self.genes[-2].weight = g.weight
        g.enabled = False
        self.nodes.append(n)
        pass

    # Get Some info
    def get_info(self) -> str:
        s = "Genome -----------------------\n"
        for g in self.genes:
            s += g.get_info()

        s += "------------------------------"
        return s

    def __str__(self):
        return self.get_info()

    # For showing
    def show(self, ds):
        ds.fill((255, 255, 255, 0))
        # Set Positions
        w, h = ds.get_size()
        vert_gap = h / (self.n_inputs + 1)
        for i in range(self.n_inputs):
            self.nodes[i].pos = [30, self.nodes[i].number * vert_gap + vert_gap]
        vert_gap = h / (self.n_outputs + 1)
        for i in range(self.n_inputs, self.n_inputs + self.n_outputs):
            self.nodes[i].pos = [
                w - 30,
                (self.nodes[i].number - self.n_inputs) * vert_gap + vert_gap,
            ]
        vert_gap = h / ((len(self.nodes) - (self.n_inputs + self.n_outputs)) + 1)
        for i in range(self.n_inputs + self.n_outputs, len(self.nodes)):
            self.nodes[i].pos = [
                w / 2,
                (self.nodes[i].number - self.n_inputs - self.n_outputs) * vert_gap
                + vert_gap,
            ]

        # Show Genes
        for g in self.genes:
            g.show(ds)
        # Show nodes
        for n in self.nodes:
            n.show(ds)
        pass
