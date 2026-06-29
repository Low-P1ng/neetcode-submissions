class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)
        end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < end:
                return False
            end = interval.end
        return True