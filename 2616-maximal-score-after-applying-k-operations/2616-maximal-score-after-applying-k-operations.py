import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
            going to use the heapq module to store the negative values
            so that we can mimic the max heap functionality
        """

        pq = []

        for num in nums:
            heapq.heappush(pq, num * -1)
        score = 0

        for i in range(0, k):
            current_element = heapq.heappop(pq) * -1
            score += current_element
            heapq.heappush(pq, math.ceil(current_element/3) * -1)
        return score
        

        