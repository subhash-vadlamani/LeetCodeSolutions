import heapq
class MedianFinder:

    def __init__(self):
        self.small_heap = [] # max-heap
        self.large_heap = [] # min_heaap
        

    def addNum(self, num: int) -> None:
        
        # add the element in in the small_heap by default
        heapq.heappush(self.small_heap, -num)

        if len(self.small_heap) - len(self.large_heap) > 1:
            popped_num = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, popped_num)
        if self.large_heap and -self.small_heap[0] > self.large_heap[0]:
            small_heap_popped_num = -heapq.heappop(self.small_heap)
            large_heap_popped_num = heapq.heappop(self.large_heap)

            heapq.heappush(self.large_heap, small_heap_popped_num)
            heapq.heappush(self.small_heap, -large_heap_popped_num)

        

    def findMedian(self) -> float:
        total_length = len(self.small_heap) + len(self.large_heap)
        if total_length % 2 != 0:
            # odd number of elements
            median = -self.small_heap[0]
            return median
        else:
            median = ((-self.small_heap[0]) + (self.large_heap[0])) / 2
        return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()