from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on the end time to minimize overlaps
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        output_count = 0  # Number of intervals to keep
        prev_end = float('-inf')  # End time of the last added interval

        for start, end in intervals:
            # If the current interval does not overlap with the last added interval
            if start >= prev_end:
                prev_end = end  # Update the last added interval's end time
                output_count += 1
            # If it overlaps, do nothing (we skip this interval)
        
        # Calculate the number of intervals to remove
        return len(intervals) - output_count