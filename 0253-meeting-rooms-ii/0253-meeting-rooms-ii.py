class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])

        # Heap to store the end times of meetings
        min_heap = [intervals[0][1]]
        min_rooms = 1

        for start, end in intervals[1:]:
            earliest_end_time = heapq.heappop(min_heap)

            if start >= earliest_end_time:
                heapq.heappush(min_heap, end)
            else:
                heapq.heappush(min_heap, earliest_end_time)
                heapq.heappush(min_heap, end)
                min_rooms += 1
        return min_rooms
        