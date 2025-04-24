class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dict = dict()

        def digit_sum(my_digit):
            current_digit_sum = 0

            while my_digit:
                current_digit_sum += (my_digit % 10)
                my_digit = my_digit // 10
            
            return current_digit_sum
        
        for i in range(1, n + 1):
            i_digit_sum = digit_sum(i)

            sum_dict[i_digit_sum] = 1 + sum_dict.get(i_digit_sum, 0)
        
        max_size = max(sum_dict.values())

        # max_size holds the max value among the values in the dict.
        # we have to count the number of keys with the the particular value

        answer = 0
        # print(sum_dict)
        for key, value in sum_dict.items():
            if value == max_size:
                answer += 1
        return answer

            

        