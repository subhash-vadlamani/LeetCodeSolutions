class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer_array = self.mergeSort(nums)
        return answer_array
    
    def merge(self, leftSortedArray, rightSortedArray):

        currentSortedArray = []
        leftPointer = 0
        rightPointer = 0

        leftSortedArrayLength = len(leftSortedArray)
        rightSortedArrayLength = len(rightSortedArray)


        while leftPointer < leftSortedArrayLength and rightPointer < rightSortedArrayLength:
            if leftSortedArray[leftPointer] < rightSortedArray[rightPointer]:
                currentSortedArray.append(leftSortedArray[leftPointer])
                leftPointer += 1
            else:
                currentSortedArray.append(rightSortedArray[rightPointer])
                rightPointer += 1
        
        while leftPointer < leftSortedArrayLength:
            currentSortedArray.append(leftSortedArray[leftPointer])
            leftPointer += 1
        
        while rightPointer < rightSortedArrayLength:
            currentSortedArray.append(rightSortedArray[rightPointer])
            rightPointer += 1
        
        return currentSortedArray
    def mergeSort(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        low = 0
        high = len(nums)
        
        mid = (low + high) // 2

        leftSortedArray = self.mergeSort(nums[low:mid])
        rightSortedArray = self.mergeSort(nums[mid: high])
        final_merged_array = self.merge(leftSortedArray, rightSortedArray)
        return final_merged_array
        