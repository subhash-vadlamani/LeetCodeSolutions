class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        arr_len = len(arr)
        good_triplet_count = 0
        prefix_cnt = [0] * 1001 # prefix counts
        # prefix_cnt[x] -> count of nums <= x
        
        for j in range(arr_len - 1):
            for k in range(j + 1, arr_len):
                if abs(arr[j] - arr[k]) <= b:
                    """
                        how many values before j
                        where abs conditions are met
                    """

                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)

                    l = max(l, 0)
                    r = min(r, 1000)

                    if l <= r:
                        good_triplet_count += prefix_cnt[r] - (0 if l == 0 else prefix_cnt[l - 1])
            
            for index in range(arr[j], 1001):
                prefix_cnt[index] += 1
        
        return good_triplet_count

        