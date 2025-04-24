import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
            Min Heap for each of the student needs to be maintained
        """

        my_dict = {} #(key -> id, value -> min heap of size 5)


        for student_id, score in items:
            if student_id not in my_dict:
                """
                    student_id does not exist in the heap.
                    create a new heap
                """
                my_heap = []
                heapq.heappush(my_heap, score)

                my_dict[student_id] = my_heap
            else:
                current_student_heap = my_dict[student_id]
                if len(current_student_heap) < 5:
                    heapq.heappush(current_student_heap, score)
                else:
                    current_min_score = current_student_heap[0]
                    if score > current_min_score:
                        heapq.heappop(current_student_heap)
                        heapq.heappush(current_student_heap, score)
                
                my_dict[student_id] = current_student_heap
        

        answer = []

        for student_id, current_student_heap in my_dict.items():
            student_average = sum(current_student_heap) // 5
            answer.append([student_id, student_average])
        
        return sorted(answer, key = lambda x: x[0])
        