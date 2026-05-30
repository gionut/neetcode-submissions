import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        dpi = dp1 = 1 # s has at least 1 character
        dp2 = 0 
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                crt = 0
            else:
                crt = dp1
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    crt += dp2
            
            crt, dp1, dp2 = 0, crt, dp1
        return dp1
        