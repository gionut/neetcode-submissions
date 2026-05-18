class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        prev = 0
        for el in nums:
            prev += el
            prefix.append(prev)
        res = 0
        table = defaultdict(int)
        for j in range(len(nums), -1, -1):
            if prefix[j] in table:
                res += table[prefix[j]]
            table[prefix[j]-k] += 1
        return res
