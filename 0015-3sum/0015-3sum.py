class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

        

        # def two_sum(nums, target, index_not_allowed):
        #     """
        #     Returns a set of frozensets, each containing two indices that add up to the target,
        #     excluding the index_not_allowed.
        #     """
        #     seen = {}
        #     two_sum_pairs = set()
        #     for j, num in enumerate(nums):
        #         if j == index_not_allowed:
        #             continue
        #         complement = target - num
        #         if complement in seen:
        #             i = seen[complement]
        #             pair = frozenset({i, j})
        #             two_sum_pairs.add(pair)
        #         seen[num] = j
        #     return two_sum_pairs
            
        
        # three_sum_indices_set = set()
        # nums_length = len(nums)

        # for i in range(0, nums_length):
        #     current_index_number = nums[i]
        #     current_target_two_sum = current_index_number * -1

        #     two_sum_indices_set_list = two_sum(nums, current_target_two_sum, i)
        #     # print(two_sum_indices_set_list)

        #     for two_sum_index_pair in two_sum_indices_set_list:
        #         current_three_sum_set = frozenset({i, *two_sum_index_pair})
        #         three_sum_indices_set.add(current_three_sum_set)
            
        # answer_set = set()
        # for three_sum_index_set in three_sum_indices_set:
        #     index1, index2, index3 = three_sum_index_set
        #     num1, num2, num3 = nums[index1], nums[index2], nums[index3]
        #     triplet = tuple(sorted([num1, num2, num3]))
        #     answer_set.add(triplet)

        # return [list(triplet) for triplet in answer_set]


        