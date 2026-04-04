class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        zero_indegree_queue = []

        def generateIndegrees(indegree, prerequisites):
            for vert, edge in prerequisites:
                indegree[vert] += 1
        
        def processZeroIndegree(vert_num):
            for vert, edge in prerequisites:
                if edge == vert_num:
                    indegree[vert] -= 1
                    if indegree[vert] == 0:
                        zero_indegree_queue.append(vert)
        
        generateIndegrees(indegree, prerequisites)
        
        for vert, indi in enumerate(indegree):
            if indi == 0:
                zero_indegree_queue.append(vert)
        
        while zero_indegree_queue != []:
            processZeroIndegree(zero_indegree_queue.pop())
            numCourses -= 1

        if numCourses == 0:
            return True
        else:
            return False
        