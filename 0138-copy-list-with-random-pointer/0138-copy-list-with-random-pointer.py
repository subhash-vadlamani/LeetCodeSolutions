"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            Use Hashmaps to store original dict
        """

        # input_dict = defaultdict(list)
        old_to_new = dict()
        head1 = head

        temp1 = head1
        pre_head2 = Node(-1)
        temp2 = pre_head2
        while temp1:
            # input_dict[temp1].append(temp1.val)
            # input_dict[temp1].append(temp1.random)

            new_node = Node(temp1.val)
            old_to_new[temp1] = new_node
            temp2.next = new_node

            temp1 = temp1.next
            temp2 = temp2.next
        
        head2 = pre_head2.next

        temp1 = head1
        temp2 = head2

        while temp1:
            temp1_random = temp1.random
            if temp1_random:
                temp2.random = old_to_new[temp1_random]
            
            temp1 = temp1.next
            temp2 = temp2.next
        
        return head2

        # hashmap to store the mapping of old to new dict
        # temp = head
        # while temp:
        