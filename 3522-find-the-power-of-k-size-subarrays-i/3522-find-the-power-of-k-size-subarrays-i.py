class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        def is_consecutively_sorted(my_list):
            prev = my_list[0]

            for i in range(1, len(my_list)):
                curr = my_list[i]
                if not (curr - prev == 1):
                    return False
                prev = curr
            return True
        
        i = 0
        j = k
        n = len(nums)
        ans = []

        while j <= n:
            curr_list = nums[i:j]
            if is_consecutively_sorted(curr_list):
                ans.append(curr_list[-1])
            else:
                ans.append(-1)
            
            i += 1
            j += 1
        return ans



        