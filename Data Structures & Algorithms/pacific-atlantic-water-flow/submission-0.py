class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        PACIFIC, ATLANTIC, BOTH = 0, 1, 2
        n, m = len(heights), len(heights[0])
        can_reach_a = set()
        can_reach_p = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = set()
        def dfs(i, j, reachable_set):
            reachable_set.add((i, j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and heights[ni][nj] >= heights[i][j] and (ni, nj) not in reachable_set:
                    dfs(ni, nj, reachable_set)
            

        for i in range(n):
            dfs(i, 0, can_reach_p)
        for j in range(m):
            dfs(0, j, can_reach_p)

        for i in range(n):
            dfs(i, m-1, can_reach_a)
        for j in range(m):
            dfs(n-1, j, can_reach_a)

        return list(can_reach_a.intersection(can_reach_p))