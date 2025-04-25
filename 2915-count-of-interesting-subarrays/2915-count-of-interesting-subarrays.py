class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        interesting_subarray_count = 0
        prefix_count = 0
        mod_freq = dict()
        mod_freq[0] = 1

        for i in range(len(nums)):
            # check if the current number is interesting

            if nums[i] % modulo == k:
                prefix_count = (prefix_count + 1) % modulo
                # mod_freq[prefix_count] = 1 + mod_freq.get(prefix_count, 0)
            
            # look for (prefix_count - k + modulo) % modulo in the hashmap

            if (prefix_count - k + modulo) % modulo in mod_freq:
                interesting_subarray_count += mod_freq[(prefix_count - k + modulo) % modulo]
            
            mod_freq[prefix_count] = 1 + mod_freq.get(prefix_count, 0)
        
        return interesting_subarray_count
