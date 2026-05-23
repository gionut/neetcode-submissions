class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        seen = {}
        for r in range(len(s)):
            while l < r and s[r] in seen:
                del seen[s[l]]
                l += 1
            seen[s[r]] = True
            res = max(r-l+1, res)
        return res