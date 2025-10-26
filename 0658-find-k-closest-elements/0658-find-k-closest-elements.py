from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Fixed version of your code: finds k closest elements to x
        using binary search + two-pointer expansion.
        """

        def perform_search():
            left, right = 0, len(arr) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    left = mid
                else:
                    right = mid

            # pick the closer index
            if abs(arr[left] - x) <= abs(arr[right] - x):
                return left
            else:
                return right

        # ---- main logic ----
        if not arr:
            return []

        required_index = perform_search()

        # create two sublists
        left_list = arr[:required_index]
        right_list = arr[required_index:]

        i = len(left_list) - 1  # left pointer
        j = 0                   # right pointer

        # expand window until k elements are selected
        while k > 0:
            if i < 0:  # no more elements on the left
                j += 1
            elif j >= len(right_list):  # no more elements on the right
                i -= 1
            else:
                if abs(x - left_list[i]) <= abs(right_list[j] - x):
                    i -= 1
                else:
                    j += 1
            k -= 1

        # slice from the original array
        left_index = max(0, i + 1)
        right_index = required_index + j
        return arr[left_index:right_index]
