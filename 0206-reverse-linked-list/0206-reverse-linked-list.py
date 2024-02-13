# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        
        if not curr_node or not curr_node.next:
            return curr_node
        else:
            while curr_node:
                nxt = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = nxt
            return prev_node
        
        