from collections import Counter
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        def is_triangle_possible(nums):
            """
                sum of the length of two sides should always be greater than or equal to the third side
            """

            combinations = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]

            for combination in combinations:
                if not (nums[combination[0]] + nums[combination[1]] > nums[combination[2]]):
                    return False
            return True

        if not is_triangle_possible(nums):
            return "none"
        side_length_counter = Counter(nums)
        max_val = float('-inf')

        for _, val in side_length_counter.items():
            if val > max_val:
                max_val = val
        
        
        if max_val == 3:
            answer = "equilateral"
        elif max_val == 2:
            answer = "isosceles"
        else:
            answer = "scalene"
        
        return answer

        