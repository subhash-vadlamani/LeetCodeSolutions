class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def verify_triplet(num1, num2, num3):
            if abs(num1 - num2) <= a and abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                return True
            return False
        

        arr_len = len(arr)
        good_triplet_count = 0
        for i in range(arr_len - 2):
            for j in range(i + 1, arr_len - 1):
                for k in range(j + 1, arr_len):
                    if verify_triplet(arr[i], arr[j], arr[k]):
                        good_triplet_count += 1
        
        return good_triplet_count

        