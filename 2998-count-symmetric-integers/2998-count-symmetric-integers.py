class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def is_number_symmetric(num):
            digit_list = []

            while num:
                digit_list.append(num % 10)
                num = num // 10
            
            digit_list_length = len(digit_list)
            if digit_list_length % 2 != 0:
                return False
            return sum(digit_list[0:digit_list_length//2]) == sum(digit_list[digit_list_length//2:])
        
        count = 0

        for num in range(low, high + 1):
            if is_number_symmetric(num):
                count += 1
        
        return count

        