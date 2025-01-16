import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
            Use Hashmap to store the numbers.
            Use Min-Heap to store the minimum
        """

        if len(hand) % groupSize != 0:
            return False
        number_of_groups = len(hand) // groupSize
        number_count_dict = dict()
        for num in hand:
            if num not in number_count_dict:
                number_count_dict[num] = 1
            else:
                number_count_dict[num] += 1
        
        min_heap = []
        for num in number_count_dict:
            heapq.heappush(min_heap, num)

        def get_current_minimum_element():
            # peek at the heap to see what is the minimum element in the heap
            while min_heap:
                heap_min = min_heap[0]
                if heap_min not in number_count_dict:
                    heapq.heappop(min_heap)
                    continue
                element_count = number_count_dict[heap_min]
                if element_count == 1:
                    required_minimum = heap_min
                    number_count_dict.pop(heap_min)
                    heapq.heappop(min_heap)
                else:
                    required_minimum = heap_min
                    number_count_dict[heap_min] -= 1
                
                return required_minimum
            return -1




        for i in range(number_of_groups):
            current_minimum = get_current_minimum_element()
            if current_minimum == -1:
                return False
            for j in range(1, groupSize):
                if (current_minimum + j) not in number_count_dict:
                    return False
                elif number_count_dict[current_minimum + j] == 1:
                    number_count_dict.pop(current_minimum + j)
                else:
                    number_count_dict[current_minimum + j] -= 1
        return True



        
        