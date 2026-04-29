class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            i, j, cnt = q.popleft()
            # if cnt > grid[i][j]:
            #     continue # stale path

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and cnt + 1 < grid[ni][nj]:
                    grid[ni][nj] = cnt + 1
                    q.append((ni, nj, cnt + 1))
 