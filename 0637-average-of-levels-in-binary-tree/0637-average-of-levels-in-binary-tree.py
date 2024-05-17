# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        answer_dict = {}
        element_queue = []

        element_queue.append((root, 1))

        while(element_queue):
            current_element = element_queue.pop(0)
            current_element_node = current_element[0]
            current_element_node_value = current_element_node.val
            current_element_level = current_element[1]

            if current_element_node.left:
                element_queue.append((current_element_node.left, current_element_level + 1))
            if current_element_node.right:
                element_queue.append((current_element_node.right, current_element_level + 1))

            
            if current_element_level  not in answer_dict:
                answer_dict[current_element_level] = [current_element_node_value]
            else:
                answer_dict[current_element_level].append(current_element_node_value)
            

        answer_list = [] 
        for level in answer_dict:
            current_level_average = round((sum(answer_dict[level]) / len(answer_dict[level])), 5)
            answer_list.append(current_level_average)
        return answer_list


        