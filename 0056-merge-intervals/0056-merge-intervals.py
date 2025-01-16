class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the intervals based on the start
        intervals.sort(key = lambda x:x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        
        return output
        