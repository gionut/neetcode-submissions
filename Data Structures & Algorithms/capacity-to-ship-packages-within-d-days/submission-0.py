class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            cnt = 0
            crt = weights[0]
            i = 0
            while i < len(weights):
                if days == cnt:
                    return False
                if i >= len(weights) - 1:
                    break
                if crt + weights[i+1] <= cap:
                    crt += weights[i+1]
                else:
                    cnt += 1
                    crt = weights[i+1]
                i += 1
            return True

        while l <= r:
            mid = l + (r-l) // 2
            print(l, r, mid)
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        