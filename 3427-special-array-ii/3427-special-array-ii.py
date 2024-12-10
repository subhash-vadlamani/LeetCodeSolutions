# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

#         """
#             Approach 1: Brute Force
#             for each and every query in the queries list, iterate through the 
#             nums list and keep checking that the consecutive numbers are of different parity.
#             If same parity encountered, break and return False. Else, return True

#             Time Complexity : O(N ** 2)
#             Verdict: Not viable given the input size
#         """

#         """
#             Hint 1: Try to split the array into some non-intersected continuous special subarrays.
#             Hint 2: For each query check that the first and the last elements of that query are in the same subarray or not
#         """

#         """
#             This is a list of lists.
#             each list contains the start and end index of a special subarray
#         """
#         continuous_special_subarrays_indices_list = []
#         """
#             Lets say, if the number is odd, the current parity is -1
#             If the number is even, the current parity is +1
#         """
#         if nums[0] % 2 == 0:
#             previous_parity = 1
#         else:
#             previous_parity = -1
        
#         current_list = [0]
#         for i in range(1, len(nums)):
#             if nums[i] % 2 == 0:
#                 current_parity = 1
#             else:
#                 current_parity = -1
            
#             if previous_parity == current_parity:
#                 current_list.append(i-1)
#                 continuous_special_subarrays_indices_list.append(current_list)
#                 current_list = [i]
            
#             previous_parity = current_parity
        
#         current_list.append(i - 1)
#         continuous_special_subarrays_indices_list.append(current_list)

        


class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[Tuple[int, int]]
    ) -> List[bool]:
        ans = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            # same parity, found violating index
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            found_violating_index = self.binarySearch(
                start + 1, end, violating_indices
            )

            if found_violating_index:
                ans[i] = False
            else:
                ans[i] = True

        return ans

    def binarySearch(
        self, start: int, end: int, violating_indices: List[int]
    ) -> bool:
        left = 0
        right = len(violating_indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            violating_index = violating_indices[mid]

            if violating_index < start:
                # check right half
                left = mid + 1
            elif violating_index > end:
                # check left half
                right = mid - 1
            else:
                # violatingIndex falls in between start and end
                return True

        return False
        