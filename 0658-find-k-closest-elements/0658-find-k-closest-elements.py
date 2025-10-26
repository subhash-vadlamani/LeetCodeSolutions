class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """

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
            
            
            if abs(x - arr[left]) <= abs(arr[right] - x):
                return left
            else:
                return right
        
        required_index = perform_search()

        left_list = arr[:required_index]
        right_list = arr[required_index:]

        i = len(left_list) - 1
        j = 0
        while k:
            if i == -1:
                j += 1
            elif j == len(arr) - required_index:
                i -= 1
            else:

                if abs(x - left_list[i]) <= abs(right_list[j] - x):
                    i -= 1
                else:
                    j += 1
            k -= 1
        
         
        return arr[max(i + 1, 0):min(required_index + j, len(arr))]
        