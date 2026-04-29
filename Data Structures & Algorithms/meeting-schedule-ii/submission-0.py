"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
(5,10),(5,20),(10,40),(40, 45)
(5,10),(5,20),(10,40),(40, 45)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted(list(map(lambda x: x.start, intervals)))
        end = sorted(list(map(lambda x: x.end, intervals)))
        s, e = 0, 0
        result, conflicts = 0, 0
        while s < n and e < n:
            if start[s] < end[e]:
                conflicts += 1
                result = max(result, conflicts)
                s += 1
            else:
                e += 1
                conflicts -= 1
        return result