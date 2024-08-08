# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 0
        high = n
        
        while low <= high:
            num = (low + high) // 2
            
            current_guess = guess(num)
            if current_guess == 0:
                return num
            elif current_guess == 1:
                low = num + 1
            else:
                high = num - 1
        