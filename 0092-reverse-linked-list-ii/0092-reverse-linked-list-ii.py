# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        current_node = head
        left_node = None
        right_node = None
        number_list = []
        count = 1
        if left == right:
            return head
        while(current_node):
            if left_node:
                number_list.append(current_node.val)
            if count == left:
                left_node = current_node
                number_list.append(current_node.val)
            
            elif count == right:
                right_node = current_node
                break
            
            current_node = current_node.next
            count += 1
        
        current_node = left_node
        for i in range(len(number_list) -1 , -1, -1):
            current_node.val = number_list[i]
            current_node = current_node.next
        return head
            
        
        