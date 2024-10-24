class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i:i[0])

        if not intervals:
            return True

        non_overlapping_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = non_overlapping_intervals[-1][1]

            if start < lastEnd:
                return False
            else:
                non_overlapping_intervals.append([start,end])
        return True
        