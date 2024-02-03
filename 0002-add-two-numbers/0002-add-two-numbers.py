# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = 0
        second_number = 0
        
        first_multiple = 1
        second_multiple = 1
        
        while(l1):
            first_number += (l1.val * first_multiple)
            first_multiple *= 10
            l1 = l1.next
        
        while(l2):
            second_number += (l2.val * second_multiple)
            second_multiple *= 10
            l2 = l2.next
            
        answer = first_number + second_number
        
        answer_node = ListNode()
        current_node = answer_node
        
        while(True):
            current_digit = answer % 10
            current_node.val = current_digit
            answer = answer // 10
            if not answer:
                break
            current_node.next = ListNode()
            current_node = current_node.next
        return answer_node
        