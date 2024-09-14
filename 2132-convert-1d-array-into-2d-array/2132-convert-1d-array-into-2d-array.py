class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Step 1 -> Make sure that an array construction is possible.

        original_list_length = len(original)
        if original_list_length != m * n:
            return []
        matrix = []
        current_original_list_index = 0

        for i in range(0, m):
            current_list = []
            for j in range(0, n):
                current_element = original[current_original_list_index]
                current_list.append(current_element)
                current_original_list_index += 1
            matrix.append(current_list)
        return matrix

        