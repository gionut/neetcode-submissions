class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.parents = [i for i in range(n+1)]
                self.size = [1] * (n+1)
            
            def find(self, u):
                pu = self.parents[u]
                if pu != u:
                    self.parents[u] = self.find(pu)
                return self.parents[u]
            
            def join(self, u, v):
                ru, rv = self.find(u), self.find(v)
                if ru == rv:
                    return False
                if self.size[ru] >= self.size[rv]:
                    self.parents[rv] = ru
                    self.size[ru] += self.size[rv]
                else:
                    self.parents[ru] = rv
                    self.size[rv] += self.size[ru]
                return True
            
        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.join(u, v):
                return [u, v]
        return []
