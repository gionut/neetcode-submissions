class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class DSU:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.size = [1] * n
            
            def find(self, u):
                root = self.parents[u]
                if u != root:
                   self.parents[u] = self.find(root)
                return self.parents[u]
            
            def join(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu == pv:
                    return False
                if self.size[pu] >= self.size[pv]:
                    self.parents[pv] = pu
                    self.size[pu] += self.size[pv]
                else:
                    self.parents[pu] = pv
                    self.size[pv] += self.size[pu]
                return True
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.join(u, v):
                return False
        return dsu.size[0] == n
                
                    