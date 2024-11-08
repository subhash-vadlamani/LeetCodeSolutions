class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
            temp -> binary string that represents the number (2 ** maximumBit) - 1

            prefix_list: prefix_list[i] = (nums[0] ^ nums[1] ^ ....... nums[i])
        """

        temp = bin(2 ** maximumBit - 1)[2:]
        # print(temp)
        n = len(nums)
        prefix_list = [0] * n
        # print(prefix_list)

        prefix_list[0] = nums[0]
        for i in range(1, n):
            prefix_list[i] = prefix_list[i-1] ^ nums[i]
        
        answer_list = []

        print(prefix_list)

        for i in range(n-1, -1, -1):
            current_prefix = prefix_list[i]
            current_prefix_binary_value = bin(current_prefix)[2:]
            current_k_binary_value = temp

            max_length = max(len(current_prefix_binary_value), len(current_k_binary_value))

            current_prefix_binary_value = current_prefix_binary_value.zfill(max_length)
            current_k_binary_value = current_k_binary_value.zfill(max_length)
            current_k_binary_value_list = list(current_k_binary_value)

            for j in range(max_length):
                if current_prefix_binary_value[j] == '0':
                    current_k_binary_value_list[j] = '1'
                else:
                    current_k_binary_value_list[j] = '0'
            
            current_answer_binary_string = "".join(current_k_binary_value_list)
            current_answer = int(current_answer_binary_string, 2)

            answer_list.append(current_answer)
        
        return answer_list
            


