class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i]
            temp += carry

            if temp // 10 == 0:
                digits[i] = temp
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
        
        if carry:
            digits = [1] + digits
        return digits


        