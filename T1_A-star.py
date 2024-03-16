from queue import PriorityQueue
from collections import deque

class A_node:
    
    def __init__(self, index) -> None:
        self.indx = index
        self.heuristic = 0
        self.successors = PriorityQueue
        self.tot_cost = int
    
    def __eq__(self, other) -> bool:
        return self.tot_cost == other.tot_cost
    
    def __lt__(self, other) -> bool:
        return self.tot_cost < other.tot_cost
    
    def __gt__(self, other) -> bool:
        return self.tot_cost > other.tot_cost


class A_star:

    def __init__(self, nodes:list[A_node], src:A_node, sink:A_node) -> None:
        self.nodes = nodes
        self.src_node = src
        self.sink_node = sink
        self.pq = PriorityQueue
        self.res = []
    
    def update(self):
        self.pq.put(self.src_node.tot_cost, item=self.src_node.indx)


n = PriorityQueue
n.put()
s = None
g = None
a = A_star(n, s, g)