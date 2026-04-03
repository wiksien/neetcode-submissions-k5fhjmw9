"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
import heapq

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def getAdjList(node):
            if not node:
                return None

            res = []

            visited = set()

            to_visit = [node]

            while to_visit:
                node_to_visit = to_visit.pop(0)

                if not node_to_visit.neighbors or node_to_visit.val in visited:
                    continue
                
                neighbour_val_list = []

                for neighbour in node_to_visit.neighbors:
                    to_visit.append(neighbour)
                    neighbour_val_list.append(neighbour.val)
                
                res.append(neighbour_val_list)
                visited.add(node_to_visit.val)

                to_visit = sorted(to_visit, key=lambda node: node.val)
            
            return res
        
        def constructFromAdjList(adj_list):
            if adj_list == None:
                return None

            if adj_list == []:
                return Node(1)

            node_list = [Node() for _ in range(len(adj_list))]

            for index, adj in enumerate(adj_list):
                node_list[index].val = index + 1

                for neighbour in adj:
                    node_list[index].neighbors.append(node_list[neighbour - 1])

            return node_list[0]
            
        return constructFromAdjList(getAdjList(node))
        