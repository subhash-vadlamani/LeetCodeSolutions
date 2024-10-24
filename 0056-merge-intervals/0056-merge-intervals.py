class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # print(output)
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


        # if len(intervals) <= 1:
        #     return intervals
        
        # sorted_intervals = sorted(intervals, key=lambda x: x[0])
        # non_overlapping_intervals = []

        # required_start = sorted_intervals[0][0]

        # for i in range(1, len(sorted_intervals)):
        #     current_start = sorted_intervals[i][0]
        #     current_end = sorted_intervals[i][1]

        #     previous_start = sorted_intervals[i-1][0]
        #     previous_end = sorted_intervals[i-1][1]

        #     if current_start > previous_end:
        #         non_overlapping_intervals.append([required_start, previous_end])
        #         required_start = current_start
        # non_overlapping_intervals.append([required_start, max(current_end, previous_end)])

        # return non_overlapping_intervals
        