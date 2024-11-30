import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
            we use a min-heap to connect the sticks
        """

        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)
        
        cost = 0
        while(len(heap) > 1):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            cost += (x + y)
            heapq.heappush(heap, x + y)
        return cost


        