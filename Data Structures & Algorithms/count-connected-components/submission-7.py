class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        
        self.rank = [0] * n

        def find_parent(vert):
            while self.parent[vert] != vert:
                vert = self.parent[vert]
            
            return vert
        
        def union(edge):
            vert1 = edge[0]
            vert2 = edge[1]

            vert1_parent = find_parent(vert1)
            vert2_parent = find_parent(vert2)

            if self.rank[vert1_parent] > self.rank[vert2_parent]:
                self.parent[vert2_parent] = self.parent[vert1_parent]
                self.rank[vert1_parent] += 1
            elif self.rank[vert1_parent] < self.rank[vert2_parent]:
                self.parent[vert1_parent] = self.parent[vert2_parent]
                self.rank[vert2_parent] += 1
            else:
                self.parent[vert2_parent] = self.parent[vert1_parent]
                self.rank[vert1_parent] += 1
            
        for edge in edges:
            union(edge)
        
        print(self.parent)
        
        return len(set([find_parent(vert) for vert in self.parent]))

        