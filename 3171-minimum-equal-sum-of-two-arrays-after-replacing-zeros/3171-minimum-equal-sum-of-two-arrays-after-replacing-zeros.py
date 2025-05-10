from collections import Counter
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_counter = Counter(nums1)
        nums1_zero_count = nums1_counter[0]
        nums2_counter = Counter(nums2)
        nums2_zero_count = nums2_counter[0]
        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)

        sum_diff = nums1_sum - nums2_sum

        print(f"nums1_sum : {nums1_sum}")
        print(f"nums1_zero_count : {nums1_zero_count}")
        print(f"nums2_sum : {nums2_sum}")
        print(f"nums2_zero_count : {nums2_zero_count}")
        print(f"sum_diff : {sum_diff}")
        

        if sum_diff > 0:
            if nums2_zero_count == 0:
                return -1
            
            if nums1_zero_count == 0:
                if nums2_zero_count > sum_diff:
                    return -1
            
            additional_amount = max(nums2_zero_count, (sum_diff + nums1_zero_count))
            min_sum = nums2_sum + additional_amount

        elif sum_diff < 0:
            if nums1_zero_count == 0:
                return - 1
            abs_sum_diff = abs(sum_diff)

            if nums2_zero_count == 0:
                if nums1_zero_count > abs_sum_diff:
                    return -1
            additional_amount = max(nums1_zero_count, (abs_sum_diff + nums2_zero_count))
            min_sum = nums1_sum + additional_amount
        else:
            if nums1_zero_count == 0 and nums2_zero_count == 0:
                additional_amount = 0
            elif nums1_zero_count == 0 or nums2_zero_count == 0:
                return -1
            
            additional_amount = max(nums1_zero_count, nums2_zero_count)
            min_sum = nums1_sum + additional_amount
        
        return min_sum



            



        