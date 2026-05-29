import functools
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @functools.lru_cache
        def f(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            cnt = i = 0
            for n in nums:
                if nums[i] > target:
                    break
                cnt += f(target-n)
            return cnt
        return f(target)
