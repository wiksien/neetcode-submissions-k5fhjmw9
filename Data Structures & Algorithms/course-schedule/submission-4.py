from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        def generateIndegreesAndGraph(indegree, prerequisites):
            for vert, edge in prerequisites:
                adj[edge].append(vert)
                indegree[vert] += 1
        
        def processZeroIndegree(vert_num):
            for edge in adj[vert_num]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    zero_indegree_queue.append(edge)
        
        generateIndegreesAndGraph(indegree, prerequisites)
        
        zero_indegree_queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while zero_indegree_queue:
            processZeroIndegree(zero_indegree_queue.popleft())
            numCourses -= 1

        if numCourses == 0:
            return True
        else:
            return False
        