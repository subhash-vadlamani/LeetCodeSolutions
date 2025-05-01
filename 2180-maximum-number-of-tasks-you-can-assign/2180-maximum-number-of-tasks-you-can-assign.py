import heapq
# class Solution:
#     import heapq
from collections import deque
from typing import List

import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Sort both lists ascending
        tasks.sort()
        workers.sort()
        
        def can_assign(k: int) -> bool:
            """
            Return True if we can assign k tasks (the k easiest) to the k strongest workers
            using at most `pills` magical pills of +strength.
            """
            if k > len(workers):
                return False
            
            # Take k strongest workers
            avail = workers[-k:].copy()
            p = pills
            
            # Try to assign tasks in descending order of difficulty
            for req in reversed(tasks[:k]):
                # 1) Try without pill: find the smallest worker >= req
                i = bisect.bisect_left(avail, req)
                if i < len(avail):
                    avail.pop(i)
                    continue
                
                # 2) Otherwise, try with a pill: find the smallest worker >= (req - strength)
                if p == 0:
                    return False
                j = bisect.bisect_left(avail, req - strength)
                if j == len(avail):
                    return False
                
                # Use a pill on that worker
                p -= 1
                avail.pop(j)
            
            return True
        
        # Binary search for the maximum k
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_assign(mid):
                left = mid
            else:
                right = mid - 1
        
        return left


# # Quick sanity checks:
# if __name__ == "__main__":
#     sol = Solution()
#     # Your failing cases:
#     print(sol.maxTaskAssign([5,9,8,5,9], [1,6,4,2,6], pills=1, strength=5))  # ➞ 3
#     print(sol.maxTaskAssign([0,4,4,8],   [3,5,0,8], pills=1, strength=3))  # ➞ 4




                





        