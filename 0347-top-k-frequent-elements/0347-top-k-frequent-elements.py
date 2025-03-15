import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count_dict = dict()
        for num in nums:
            if num not in num_count_dict:
                num_count_dict[num] = 1
            else:
                num_count_dict[num] += 1
        
        num_count_list = [[] for _ in range(len(nums) + 1)] 

        for _, (key, val) in enumerate(num_count_dict.items()):
            num_count_list[val].append(key)
        
        answer_list = []
        current_count = 0
        # print(num_count_list)

        for i in range(len(num_count_list) - 1, 0, -1):
            if num_count_list[i]:
                for j in range(len(num_count_list[i])):
                    answer_list.append(num_count_list[i][j])
                    current_count += 1
                    if current_count == k:
                        break
            if current_count == k:
                break
        return answer_list

        
        # heap = []
        # for index, (key, val) in enumerate(num_count_dict.items()):
        #     if len(heap) < k:
        #         heapq.heappush(heap, [val, key])
        #     else:
        #         if val > heap[0][0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, [val, key])
        # # print(heap)
        # answer = []
        # for i in range(len(heap)):
        #     answer.append(heap[i][1])
        # return answer
        