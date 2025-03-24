class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)

        free_days = 0

        prev = meetings[0]
        free_days += (prev[0] - 1)
        for i in range(1, len(meetings)):
            meeting = meetings[i]
            prev_end = prev[1]
            current_end = meeting[1]
            if meeting[0] > prev_end:
                free_days += (meeting[0] - prev[1] - 1)
            prev = meeting
            prev[1] = max(prev_end, current_end)
        
        free_days += (days - prev[1])

        return free_days

        
        