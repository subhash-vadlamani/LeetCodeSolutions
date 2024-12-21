class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sliding_window_dict = dict()
        answer = []
        current_max = float('-inf')

        l = 0
        for r in range(len(nums)):
            sliding_window_dict[nums[r]] = 1 + sliding_window_dict.get(nums[r], 0)

            if r - l + 1 == k:
                if current_max == float('-inf'):
                    current_max = max(sliding_window_dict.keys())
                else:
                    current_max = max(current_max, nums[r])

                answer.append(current_max)

                if sliding_window_dict[nums[l]] > 1:
                    sliding_window_dict[nums[l]] -= 1
                else:
                    del sliding_window_dict[nums[l]]
                    if current_max == nums[l]:
                        if sliding_window_dict.keys():
                            current_max = max(sliding_window_dict.keys())
                        else:
                            current_max = float('-inf')
                
                l += 1
                
        return answer


        