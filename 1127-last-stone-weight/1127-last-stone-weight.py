import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            we use max-heap and we run a loop of breaking the stones
            till there is only one stone left in the heap.

            We will use negative weight of the stones to simulate max-heap
        """

        heap = []

        for i in range(len(stones)):
            negative_stone_weight = -stones[i]
            heapq.heappush(heap, negative_stone_weight)
        
        while len(heap) > 1:
            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1

            weight_difference = y - x
            if weight_difference > 0:
                heapq.heappush(heap, -weight_difference)
        

        return heap[0] * -1 if len(heap) == 1 else 0






        