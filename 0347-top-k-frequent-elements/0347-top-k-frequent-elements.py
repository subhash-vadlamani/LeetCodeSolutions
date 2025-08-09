import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # కె మోస్ట్ ఫ్రీక్వెంట్ ఎలిమెంట్స్ రిటర్న్ చేయాలి 
        # calculate the freq dict and insert them into min heap of size k
        # Time complexity: O(N * log(k))

        freq_dict = dict()
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        min_heap = [] # Each element will be of the format (freq, element)
        count = 0

        for key in freq_dict:
            freq_value = freq_dict[key]
            heap_element = (freq_value, key)

            if count < k:
                heapq.heappush(min_heap, heap_element)
                count += 1
            else:
                top_element_freq = min_heap[0][0]
                if freq_value > top_element_freq:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, heap_element)
        
        answer = []
        while min_heap:
            answer.append(heapq.heappop(min_heap)[1])
        return answer



