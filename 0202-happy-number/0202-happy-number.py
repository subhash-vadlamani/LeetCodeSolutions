class Solution:
    def isHappy(self, n: int) -> bool:
        
        result = n
        while result !=1 and result != 4:
            result = self.getSquareSum(result)
        if result == 1:
            return True
        else:
            return False
    
    def getSquareSum(self, num):
        sum = 0
        
        while num>0:
            rem = num % 10
            sum += (rem * rem)
            num = num // 10
        return sum
        