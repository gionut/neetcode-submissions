class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n, nfreq in cnt.items():
            freq[nfreq].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            if freq[i]:
                res.extend(freq[i])
            if len(res) == k:
                break
        return res
