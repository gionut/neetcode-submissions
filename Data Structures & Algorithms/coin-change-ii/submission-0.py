#                     0
#         1=2           2       3=1
#     2=1   3=1   4=0
# 3=1   4=0   5=0
import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @functools.lru_cache(None)
        def f(i, crt):
            if crt == amount:
                return 1
            if crt > amount:
                return 0 
            
            res = 0
            for ci in range(i, len(coins)):
                res += f(ci, crt + coins[ci])
            return res

        return f(0, 0)