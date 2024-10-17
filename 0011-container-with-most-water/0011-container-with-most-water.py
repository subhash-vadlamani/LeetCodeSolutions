class Solution:
    def maxArea(self, height: List[int]) -> int:
        list_length = len(height)
        max_area = 0
        i = 0
        j = list_length - 1

        while i < j:
            i_height_value = height[i]
            j_height_value = height[j]

            current_area = min(i_height_value, j_height_value) * (j - i)
            if current_area > max_area:
                max_area = current_area

            if i_height_value <= j_height_value:
                i += 1
            else:
                j -= 1
        return max_area


        