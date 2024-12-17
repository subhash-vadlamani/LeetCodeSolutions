import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Min Heap and a element count dict

        num_count_dict = dict()
        for num in nums:
            if num not in num_count_dict:
                num_count_dict[num] = 1
            else:
                num_count_dict[num] += 1
        
        heap = []
        for index, (key, val) in enumerate(num_count_dict.items()):
            if len(heap) < k:
                heapq.heappush(heap, [val, key])
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [val, key])
        # print(heap)
        answer = []
        for i in range(len(heap)):
            answer.append(heap[i][1])
        return answer
        