class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        actual_nums = []
        actual_num_dict = dict()

        for num in nums:
            current_actual_num = 0
            temp = num
            current_multiple = 1
            if num == 0:
                current_actual_num = mapping[num]
                actual_nums.append(current_actual_num)
                if current_actual_num not in actual_num_dict:
                    actual_num_dict[current_actual_num] = [temp]
                else:
                    actual_num_dict[current_actual_num].append(temp)
                continue
            while num:
                current_digit = num % 10
                current_actual_digit = mapping[current_digit]
                current_actual_num = current_actual_num  + current_actual_digit * current_multiple
                num = num // 10
                current_multiple *= 10
            actual_nums.append(current_actual_num)
            if current_actual_num not in actual_num_dict:
                actual_num_dict[current_actual_num] = [temp]
            else:
                actual_num_dict[current_actual_num].append(temp)
        
        actual_nums.sort()
        for i in range(0, len(nums)):
            actual_nums[i] = actual_num_dict[actual_nums[i]].pop(0)
        return actual_nums


        