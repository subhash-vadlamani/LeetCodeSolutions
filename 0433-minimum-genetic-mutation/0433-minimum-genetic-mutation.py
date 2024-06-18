from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def get_character_differences(str1, str2, length):

            count = 0

            for i in range(0, length):
                if str1[i] != str2[i]:
                    count += 1
            return count


        queue = deque()
        string_length = len(startGene)

        queue.append((startGene, 0))

        visited_set = set()

        while queue:
            current_string, current_count = queue.popleft()

            if current_string in visited_set:
                continue

            if current_string == endGene:
                return current_count

            visited_set.add(current_string)

            for string in bank:
                if get_character_differences(string, current_string, string_length) == 1:
                    queue.append((string, current_count + 1))
        
        return -1

        


        