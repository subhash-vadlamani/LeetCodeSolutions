# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            known_count = 0

            for j in range(n):
                if i != j:
                    if knows(i, j) or not knows(j, i):
                        break
                    
                    known_count += 1
            if known_count == n-1:
                return i
        
        return -1
        