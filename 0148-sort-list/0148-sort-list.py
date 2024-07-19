# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def perform_merge_sort(self, element_list):

        def merge(array, begin, mid, end):
            subArrayOne = mid - begin + 1
            subArrayTwo = end - mid

            leftArray = [0] * subArrayOne
            rightArray = [0] * subArrayTwo

            for i in range(subArrayOne):
                leftArray[i] = array[begin + i]
            for j in range(subArrayTwo):
                rightArray[j] = array[mid + 1 + j]
            
            indexOfSubArrayOne = 0
            indexOfSubArrayTwo = 0
            indexOfMergedArray = begin

            while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
                if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                    array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                    indexOfSubArrayOne += 1
                else:
                    array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                    indexOfSubArrayTwo += 1
                
                indexOfMergedArray += 1
            
            while indexOfSubArrayOne < subArrayOne:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
                indexOfMergedArray += 1
            
            while indexOfSubArrayTwo < subArrayTwo:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
                indexOfMergedArray += 1

        def merge_sort(array, begin, end):
            if begin >= end:
                return
            
            mid = begin + (end - begin) // 2
            merge_sort(array, begin, mid)
            merge_sort(array, mid + 1, end)
            merge(array, begin ,mid, end)
        
        merge_sort(element_list, 0, len(element_list) - 1)
        return element_list

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A simple solution would be to convert the list into an array
        # perform merge sort on it and then return a new array

        if not head:
            return None

        element_list = []
        temp = head

        while temp:
            element_list.append(temp.val)
            temp = temp.next
        
        sorted_element_list = self.perform_merge_sort(element_list)

        new_head = ListNode(val = sorted_element_list[0])
        temp = new_head
        for i in range(1, len(sorted_element_list)):
            temp.next = ListNode(sorted_element_list[i])
            temp = temp.next
        return new_head
    

        
        
        
        
    
        
        