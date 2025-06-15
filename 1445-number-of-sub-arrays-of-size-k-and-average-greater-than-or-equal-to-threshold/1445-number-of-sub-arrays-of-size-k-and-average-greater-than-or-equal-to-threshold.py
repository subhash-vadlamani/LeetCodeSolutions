class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
            sliding window?
        """

        i = 0
        j = k
        required_subarray_count = 0
        current_sum = sum(arr[i:j])
        # current_average = current_sum / k
        
        while j <= len(arr):
            current_average = current_sum / k
            if current_average >= threshold:
                required_subarray_count += 1
            
            current_sum -= arr[i]
            i += 1
            j += 1
            if j > len(arr):
                break
            current_sum += arr[j-1]
        
        return required_subarray_count

            
        