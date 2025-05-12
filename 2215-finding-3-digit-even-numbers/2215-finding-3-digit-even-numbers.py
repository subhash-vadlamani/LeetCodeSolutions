from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []

        def dfs(pos, digit_count, current_num):
            if pos == 3:
                ans.append(int(current_num))
                return

            # Decide valid digit range
            start = 1 if pos == 0 else 0
            end = 10

            for d in range(start, end):
                # Only allow even digits at last position
                if pos == 2 and d % 2 != 0:
                    continue

                if digit_count[d] > 0:
                    new_count = digit_count.copy()
                    new_count[d] -= 1
                    dfs(pos + 1, new_count, current_num + str(d))

        digit_count = Counter(digits)
        dfs(0, digit_count, "")
        return sorted(set(ans))
