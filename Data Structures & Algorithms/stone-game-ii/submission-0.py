import functools
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n)
        s = 0
        for i in range(n-1, -1, -1):
            s += piles[i]
            suffix[i] = s
        @functools.lru_cache(None)
        def f(l, m):
            if l == n:
                return 0
            
            res = 0
            for x in range(1, m*2+1):
                r = l + x
                if r > n:
                    break
                res = max(res, suffix[l] - f(r, max(m, x)))
            return res
        return f(0, 1)