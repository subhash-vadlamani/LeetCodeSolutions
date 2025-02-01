# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next or not head.next.next:
            return

        def reverse_list(node):
            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        

        def get_second_list_head(node):
            slow = node
            fast = node

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            second_half = slow.next
            slow.next = None
            return second_half
        

        temp = head
        head1 = head
        head2 = reverse_list(get_second_list_head(temp))

        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2
        
        