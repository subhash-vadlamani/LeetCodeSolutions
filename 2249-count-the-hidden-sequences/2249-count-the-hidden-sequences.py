class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        diff_list = [0]

        for i in range(len(differences)):
            diff_list.append(diff_list[-1] + differences[i])
        
        diff_list.sort()

        new_lower = lower + abs(diff_list[0])
        new_upper = upper - abs(diff_list[-1])

        answer = new_upper - new_lower + 1

        return answer if answer >= 0 else 0

        