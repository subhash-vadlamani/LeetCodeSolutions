import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        temp = head

        while True:
            """
                We maintain a list of that contains 2 elements
                1. The minimum element encountered so far
                2. Index of the list of linkedlist where the minimum element was found
            """
            min_element_list = [float('inf'), None]
            for i in range(len(lists)):
                lst = lists[i]
                if lst and lst.val < min_element_list[0]:
                    min_element_list = [lst.val, i]
            if min_element_list[0] != float('inf'):
                if not head:
                    head = ListNode()
                    temp = head
                    temp.val = min_element_list[0]
                else:
                    temp.next = ListNode()
                    temp = temp.next
                    temp.val = min_element_list[0]

                lists[min_element_list[1]] = lists[min_element_list[1]].next
            else:
                break
        
        return head




        