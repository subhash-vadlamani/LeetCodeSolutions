import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}
        NEG_INF = - 10 ** 20
        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 1
            else:
                task_dict[task] += 1
        heap = []
        #(time_last_used, task, task_count)
        for _, (key, val) in enumerate(task_dict.items()):
            heapq.heappush(heap, (NEG_INF, key, val))
        
        order_list = []
        i = 1

        while True:
            if not heap:
                break
            current_max_freq_tuple = (None, None, NEG_INF)
            popped_tuples = []
            while heap and (heap[0][0] == NEG_INF or i - heap[0][0] > n):
                current_popped_tuple = heapq.heappop(heap)
                if current_popped_tuple[2] > current_max_freq_tuple[2]:
                    current_max_freq_tuple = current_popped_tuple
                popped_tuples.append(current_popped_tuple)
            # print("i = {} and popped_tuples = {}".format(i, popped_tuples))
            if popped_tuples:
                current_max_freq_key = current_max_freq_tuple[1]
                current_max_freq_val = current_max_freq_tuple[2]
                order_list.append(current_max_freq_key)
                if current_max_freq_val > 1:
                    heapq.heappush(heap, (i, current_max_freq_key, current_max_freq_val - 1))
                # time to push remaining keys
                for j in range(len(popped_tuples)):
                    if popped_tuples[j][1] != current_max_freq_key:
                        heapq.heappush(heap, popped_tuples[j])
            else:
                # "*" means idle
                order_list.append("*")
            i += 1
        # print(order_list)
        return len(order_list)


        # while True:
        #     if not heap:
        #         break
        #     current_head = heap[0]
        #     if current_head[0] == NEG_INF or i - current_head[0] > n:
        #         popped_head = heapq.heappop(heap)
        #         popped_head_key = popped_head[1]
        #         popped_head_val = popped_head[2]
        #         order_list.append(popped_head_key)
        #         if popped_head_val > 1:
        #             heapq.heappush(heap, (i, popped_head_key, popped_head_val - 1))
        #     else:
        #         # "*" means idle
        #         order_list.append("*")
        #     i += 1
        # print(order_list)
        # return len(order_list)



        



        