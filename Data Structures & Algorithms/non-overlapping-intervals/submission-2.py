class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s < end:
                end = min(e, end)
                res += 1
            else:
                end = e
        return res