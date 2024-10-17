import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res

        # pq = []
        # heapq.heappush(pq, ( -a, 'a'))
        # heapq.heappush(pq, (-b, 'b'))
        # heapq.heappush(pq, (-c, 'c'))

        # longest_possible_happy_string = ""

        # def heap_push_elements(pq, element_list):
        #     for element in element_list:
        #         heapq.heappush(pq, element)

        # while True:
        #     current_pq_list = []
        #     while pq:
        #         current_pq_list.append(heapq.heappop(pq))
            
        #     if len(longest_possible_happy_string) < 2:
        #         character_to_append = current_pq_list[0][1]
        #         character_to_append_count = current_pq_list[0][0] * -1

        #         longest_possible_happy_string += character_to_append
        #         character_to_append_count -= 1

        #         if character_to_append_count == 0:
        #             current_pq_list.pop(0)
        #         else:
        #             current_pq_list[0] == (character_to_append_count * -1, character_to_append)
        #     else:
        #         character_to_append = current_pq_list[0][1]
        #         character_to_append_count = current_pq_list[0][0] * -1

        #         last_two_characters = longest_possible_happy_string[-2:]
        #         if last_two_characters == character_to_append + character_to_append:
        #             if len(current_pq_list) == 1:
        #                 return longest_possible_happy_string
        #             else:
        #                 character_to_append = currrent_pq_list[1][1]
        #                 character_to_append_count = current_pq_list[1][0] * -1










        