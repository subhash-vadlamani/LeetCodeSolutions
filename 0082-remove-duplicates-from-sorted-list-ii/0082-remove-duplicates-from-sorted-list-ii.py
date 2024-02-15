# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        number_dict = {}
        temp_node = head
        
        while temp_node:
            if temp_node.val not in number_dict:
                number_dict[temp_node.val] = 1
            else:
                number_dict[temp_node.val] += 1
            temp_node = temp_node.next
            
        
        unique_numbers = []
        temp_node = head
        
        while temp_node:
            if number_dict[temp_node.val] == 1:
                unique_numbers.append(temp_node.val)
                
            temp_node = temp_node.next
        
        if not unique_numbers:
            return None
        temp_node = head
        for i in range(0, len(unique_numbers) - 1):
            temp_node.val = unique_numbers[i]
            temp_node = temp_node.next
        temp_node.val= unique_numbers[-1]
        temp_node.next = None
        
        return head
            
        
        
        