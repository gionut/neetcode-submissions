class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        VISITED = "*"
        LAND = "1"
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != LAND:
                return
            
            grid[i][j] = VISITED
            for di, dj in dirs:
                dfs(i + di, j + dj)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == LAND:
                    dfs(i, j)
                    count += 1
        
        return count