class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        self.count = n

        def find_parent(vert):
            if parent[vert] == vert:
                return vert
            
            parent[vert] = find_parent(parent[vert])
            return parent[vert]
        
        def union(edge):
            vert1 = edge[0]
            vert2 = edge[1]

            root1 = find_parent(vert1)
            root2 = find_parent(vert2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
    
                self.count -= 1
            
        for edge in edges:
            union(edge)
        
        return self.count

        