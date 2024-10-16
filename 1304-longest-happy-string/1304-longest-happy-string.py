import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for i, freq in enumerate([a,b,c]):
            if freq > 0:
                heapq.heappush(heap, (-freq, chr(i + ord('a'))))
        heapq.heapify(heap)
        ans = []
        while heap and len(heap) > 1:
            add_later = []
            val,char = heapq.heappop(heap)
            val2,char2 = heapq.heappop(heap)

            val = -val
            val2 = -val2
            if val == 1:
                ans.append(char)
                val -= 1
            else:
                if (ans and char != ans[-1]) or not ans:
                    ans.append(char*2)
                    val -= 2
                else:
                    ans.append(char)
                    val -= 1
            if val2 >= 1:
                ans.append(char2)
                val2 -= 1
            if val > 0:
                add_later.append((-val,char))
            if val2 > 0:
                add_later.append((-val2,char2))
            for v,ch in add_later:
                heapq.heappush(heap, (v,ch))
        if heap and -heap[0][0] > 0:
            val,ch = heap[0]
            val = -val
            if val == 1:
                ans.append(ch)
            else:
                ans.append(ch*2)
        return "".join(ans)
        # pq = []
        # pq.heappush('a', -a)
        # pq.heappush('b', -b)
        # pq.heappush('c', -c)

        # longest_possible_happy_string = ""

        # def heap_push_elements(pq, element_list):
        #     for element in element_list:
        #         pq.heappush()

        # while True:
        #     current_pq_list = []
        #     while pq:
        #         current_pq_list.append(pq.heappop())
            
        #     if len(longest_possible_happy_string) < 2:
        #         character_to_append = current_pq_list[0][0]
        #         character_to_append_count = current_pq_list[0][1] * -1

        #         longest_possible_happy_string += character_to_append
        #         character_to_append_count -= 1

        #         if character_to_append_count == 0:
        #             current_pq_list.pop(0)
        #         else:
        #             current_pq_list[0] == (character_to_append, character_to_append_count * -1)







        