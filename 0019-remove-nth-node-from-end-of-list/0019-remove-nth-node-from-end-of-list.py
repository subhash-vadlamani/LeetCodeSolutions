# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list_length = 0
        temp_node = head
        
        while temp_node:
            linked_list_length += 1
            temp_node = temp_node.next
        front_node_number = (linked_list_length + 1) - n
        
        if front_node_number == 1:
            head = head.next
            return head
        
        current_node_number = 2
        
        temp_node = head
        
        while current_node_number < front_node_number:
            temp_node = temp_node.next
            current_node_number += 1
        if temp_node.next:
            temp_node.next = temp_node.next.next
        # else:
        #     head = None
        return head
        