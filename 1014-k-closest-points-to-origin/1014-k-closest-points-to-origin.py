import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(point):
            x = point[0]
            y = point[1]

            distance = math.sqrt(x ** 2 + y ** 2)
            return distance
        
        heap = []
        #max heap of size k
        for i in range(len(points)):
            current_distance = distance_from_origin(points[i])
            heapq.heappush(heap, (-current_distance, points[i]))
            if i >= k:
                heapq.heappop(heap)
        answer_list = []
        while heap:
            answer_list.append(heapq.heappop(heap)[1])
        return answer_list

        