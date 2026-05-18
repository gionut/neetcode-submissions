class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        table[0] = 1
        curr = res = 0
        for el in reversed(nums):
            curr += el
            if curr - k in table:
                res += table[curr - k]
            table[curr] += 1
        return res
