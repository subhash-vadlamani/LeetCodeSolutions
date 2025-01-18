class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        elif n == 0:
            return 1
        
        seen = {}
        if n < 0:
            x = 1/x
            n *= -1
        def calculate(n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            if n in seen:
                return seen[n]
            
            if n % 2 == 0:
                ans = calculate(n // 2)
                ans = ans * ans
            else:
                ans = calculate(n // 2) * calculate((n // 2) + 1 )
            
            seen[n] = ans
            return ans
        
        return calculate(n)
                
        