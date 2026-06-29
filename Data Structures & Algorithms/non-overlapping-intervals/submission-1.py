class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        intervals.pop(0)
        res = 0
        for s, e in intervals:
            if s < end:
                end = min(e, end)
                res += 1
            else:
                end = e
        return res