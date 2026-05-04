class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(board)
        m = len(board[0])
        sides = []
        def dfs(i, j):
            board[i][j] = "M"
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == "O":
                    dfs(ni, nj)

        # Save Os on the sides
        for i in range(n):
            if board[i][0] == "O":
                sides.append((i, 0))
            if board[i][m-1] == "O":
                sides.append((i, m-1))
        for j in range(m):
            if board[0][j] == "O":
                sides.append((0, j))
            if board[n-1][j] == "O":
                sides.append((n-1, j))
        
        # DFS to mark sidefacing O regions to Ms
        for i, j in sides:
            if board[i][j] == "O":
                dfs(i, j)
        
        # Turn remaining Os to Xs
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # Turn Ms regions back to Os
        for i in range(n):
            for j in range(m):
                if board[i][j] == "M":
                    board[i][j] = "O"
            