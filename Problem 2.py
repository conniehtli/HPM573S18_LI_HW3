class Node:
    """ base class """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """
        abstract method to be overridden in derived classes
        :returns expected cost of this node
        """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs, health_utility):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs
        self.healthUtility = health_utility

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_health_utility(self):
        exp_health_utility = self.healthUtility  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_health_utility += self.probs[i] * node.get_expected_health_utility()
            i += 1
        return exp_health_utility

class TerminalNode(Node):

    def __init__(self, name, cost, health_utility):
        Node.__init__(self, name, cost)
        self.healthUtility = health_utility

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_health_utility(self):

        return self.healthUtility

class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes, health_utility):
        Node.__init__(self, name, cost)
        self.futureNode = future_nodes
        self.healthUtility = health_utility

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()

        return outcomes

    def get_expected_health_utility(self):
        outcomes = dict()  # dictionary to store the expected health utility of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_health_utility()

        return outcomes

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2
C2 = ChanceNode('C2', 35, [T1, T2], [0.7, 0.3], 0)
# create C1
C1 = ChanceNode('C1', 25, [C2, T3], [0.2, 0.8], 0)
# create C3
C3 = ChanceNode('C3', 45, [T4, T5], [0.1, 0.9], 0)

# create D1
D1 = DecisionNode('D1', 0, [C1, C3], 0)

# print the expect cost of C1
print('Expected cost', D1.get_expected_costs())
print('Expected health utility', D1.get_expected_health_utility())
