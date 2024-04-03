class GeneHistory:
    def __init__(self, n_inputs, n_outputs):
        # no of Inputs (int)
        self.n_inputs = n_inputs
        # no of outputs(int)
        self.n_outputs = n_outputs
        # All Genes in existence
        self.all_genes = []
        # Global highest innovation
        self.global_inno = 0
        # Highest hidden layer(index)
        self.highest_hidden = 3  # i.e max 2 hidden layers
        pass

    # Check if already exists in history
    def exists(self, n1, n2):
        for g in self.all_genes:
            if g.in_node.number == n1.number and g.out_node.number == n2.number:
                return g.clone()
        return None
