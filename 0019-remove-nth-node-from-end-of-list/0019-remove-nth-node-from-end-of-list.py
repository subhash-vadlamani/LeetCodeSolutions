# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #calculate the length of the list

        linked_list_length = 0
        temp = head
        while temp:
            temp = temp.next
            linked_list_length += 1
        
        # Now, we calculate the number of the node from front

        number_from_front = linked_list_length - n + 1

        """
            stop the loop when you reach the node whose number
            is one less than the node you want to remove
        """

        current_node = head
        current_node_number = 1

        if number_from_front == 1:
            return head.next
        while True:
            if current_node_number == number_from_front - 1:
                break
            current_node = current_node.next
            current_node_number += 1
        
        current_node.next = current_node.next.next

        return head
        
            

        