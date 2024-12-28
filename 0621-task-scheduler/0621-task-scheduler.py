import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
            Max Heap to store frequencies
            Queue to store when the element is available to be pushed to the heap again
            continue till the heap is empty
        """

        heap = []
        task_dict = {}
        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 1
            else:
                task_dict[task] += 1
        
        for _, (key, val) in enumerate(task_dict.items()):
            heapq.heappush(heap, -val)
        
        # Max heap ready

        queue = deque()
        # popleft method to simulate the queue

        minimum_cpu_intervals = 0
        i = 1
        while heap or queue:
            if queue and queue[0][1] < i:
                heapq.heappush(heap, queue.popleft()[0])

                # while queue and queue[0][1] < i:
                #     heapq.heappush(heap, queue.popleft()[0])
            if heap:
                current_element_freq = heapq.heappop(heap)
                if current_element_freq < -1:
                    queue.append((current_element_freq + 1, i + n))
            
            minimum_cpu_intervals += 1
            i += 1
        return minimum_cpu_intervals



        