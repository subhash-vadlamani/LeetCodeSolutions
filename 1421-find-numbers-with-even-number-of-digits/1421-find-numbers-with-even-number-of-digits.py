class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def compute_digit_count(my_number):
            my_digit_count = 0

            while my_number:
                my_digit_count += 1
                my_number = my_number // 10
            
            return my_digit_count
        
        answer = 0

        for num in nums:
            if compute_digit_count(num) % 2 == 0:
                answer += 1
        return answer
        