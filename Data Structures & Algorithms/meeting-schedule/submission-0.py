class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)
        for i in range(1, n):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True