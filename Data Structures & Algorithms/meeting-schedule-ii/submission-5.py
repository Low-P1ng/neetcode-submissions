"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        startl = []
        endl = []
        for interval in intervals:
            startl.append(interval.start)
            endl.append(interval.end)
        startl.sort();endl.sort()
        res = si = ei = count = 0
        while si < len(startl):
            if startl[si]<endl[ei]:
                res+=1
                si += 1
            else:
                res-=1
                ei += 1
            count = max(res,count)
        return count