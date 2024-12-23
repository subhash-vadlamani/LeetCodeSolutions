import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.heap, nums[i])
            else:
                heapq.heappush(self.heap, nums[i])
                heapq.heappop(self.heap)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)