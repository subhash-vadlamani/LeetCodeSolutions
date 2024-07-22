class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        height_dict = dict()

        for i in range(0, len(heights)):
            height_dict[i] = heights[i]
        
        sorted_items = sorted(height_dict.items(), key=lambda item: item[1], reverse=True)

        final_name_list = []

        for key, _ in sorted_items:
            final_name_list.append(names[key])
        return final_name_list
        