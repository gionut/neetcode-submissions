class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])
        result = 0
        crt, ref = 1, 0
        while crt < n:
            if intervals[crt][0] < intervals[ref][1]:
                result += 1
                if intervals[crt][1] < intervals[ref][1]:
                    ref = crt
            else:
                ref = crt
            crt += 1
        return result