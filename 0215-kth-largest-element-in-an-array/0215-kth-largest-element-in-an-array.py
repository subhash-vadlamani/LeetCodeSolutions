import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        """
            For finding the kth largest number, we are going to maintain
            a min-heap
        """

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, nums[i])
                heapq.heappop(heap)
        return heap[0]
        