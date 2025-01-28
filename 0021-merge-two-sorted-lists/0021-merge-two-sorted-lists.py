# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(val = -101)
        temp = head
        prev = None
        # Case1: list1 & list2 point to non null nodes
        while list1 and list2:
            list1_val = list1.val
            list2_val = list2.val

            if list1_val < list2_val:
                temp.val = list1_val
                list1 = list1.next
            else:
                temp.val = list2_val
                list2 = list2.next
            
            prev = temp
            temp.next = ListNode()
            temp = temp.next
        
        """
            When we break out of this loop, the node pointed by the prev node should be our last node
        """
        if prev:
            prev.next = None
            temp = prev
        # Case2: only list1 points to non null node
        while list1:
            temp.next = ListNode()
            temp = temp.next
            temp.val = list1.val
            list1 = list1.next
        # Case3: only list2 points to non null node
        while list2:
            temp.next = ListNode()
            temp = temp.next
            temp.val = list2.val
            list2 = list2.next
        
        if head.val == -101:
            return head.next
        else:
            return head
        