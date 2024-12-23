from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.my_map = defaultdict(lambda: [[], []])

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_map[key][0].append(timestamp)
        self.my_map[key][1].append(value)

        

    def get(self, key: str, timestamp: int) -> str:
        def perform_binary_search(nums, target):
            """
                If the target is found, we have to return the index of the target.
                If the target is not found, we have to return the index of the 
                largest number in nums that is less than target
            """

            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + ((high - low) // 2)

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low - 1

        if not self.my_map[key][0] or timestamp < self.my_map[key][0][0]:
            return ""     
        required_index = perform_binary_search(self.my_map[key][0], timestamp)
        return self.my_map[key][1][required_index]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)