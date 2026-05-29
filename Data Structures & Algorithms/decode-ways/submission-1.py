# 10 13   - 9 -   8   -   2   -   7
#    1    - 3 -   9   -   8   -   2   -   7
# 10  -   13  -   09827 X
#     -   1   -   309827
# f(101398224) = f(1398224)6
# f(1398224) = f(398224) + f(98224) 6
# f(398224) = f(98224) 3
# f(98224) = f(8224) 3
# f(8224) = f(224) 3
# f(224) = f(24) + f(4) = 3 
# f(24) = 1 + (4) = 2
# f(4) = 1  
import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache
        def f(s):
            if len(s) == 0:
                return 1

            if len(s) == 1 and int(s[0]) > 0:
                return 1

            if int(s[0]) == 0:
                return 0

            if int(s[0]) > 2:
                return f(s[1:])
            
            if len(s) > 1 and int(s[:2]) <= 26:
                return f(s[1:]) + f(s[2:])
            
            return f(s[1:])
        return f(s)

        