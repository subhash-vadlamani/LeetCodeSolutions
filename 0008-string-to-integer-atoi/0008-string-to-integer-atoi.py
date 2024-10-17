class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        is_positive = True
        if s[0] == '-':
            is_positive = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        non_zero_digit_encountered = False
        char_digit_set = {'0', '1', '2', '3', '4', '5', '6', '7' ,'8', '9'}
        digit_list = []

        for char in s:
            if char not in char_digit_set:
                break
            elif char == '0' and not non_zero_digit_encountered:
                continue
            elif char == '0' and non_zero_digit_encountered:
                digit_list.append(int(char))
            else:
                digit_list.append(int(char))
                non_zero_digit_encountered = True
        
        ans = 0
        current_multiple = 1

        for i in range(len(digit_list) - 1, -1, -1):
            ans += digit_list[i] * current_multiple
            current_multiple *= 10
        
        if not is_positive:
            ans *= -1
        
        if ans < -1 * 2 ** 31:
            ans = -1 * 2 ** 31
        elif ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        
        return ans
            


        
        