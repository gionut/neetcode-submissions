class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n, m = len(board), len(board[0])

        def backtrack(i, j, crt):
            if crt == len(word):
                return True
            
            if not (0 <= i < n and 0 <= j < m) or board[i][j] != word[crt]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'
            
            found = False
            for di, dj in dirs:
                found |= backtrack(i + di, j + dj, crt + 1)
            
            board[i][j] = tmp
            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False

        

