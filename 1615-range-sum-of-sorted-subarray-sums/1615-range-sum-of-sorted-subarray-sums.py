class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_list_sum_list = []

        for i in range(0, n):
            current_sub_list_sum = 0
            for j in range(i, n):
                current_sub_list_sum += nums[j]
                sub_list_sum_list.append(current_sub_list_sum)
        
        answer = 0
        sub_list_sum_list.sort()

        for i in range(left-1, right):
            answer += sub_list_sum_list[i]
        
        answer = answer % (10 ** 9 + 7)
        return answer

        