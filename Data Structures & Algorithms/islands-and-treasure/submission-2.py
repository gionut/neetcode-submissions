class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        cnt = 1
        while q:
            lvl = len(q)
            for _ in range(lvl):
                i, j = q.popleft()

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and cnt < grid[ni][nj]:
                        grid[ni][nj] = cnt
                        q.append((ni, nj))
            cnt += 1
 