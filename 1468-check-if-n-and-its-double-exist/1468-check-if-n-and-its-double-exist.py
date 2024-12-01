class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        number_set = set()

        for num in arr:
            if num % 2 == 0:
                if int(num // 2) in number_set:
                    return True
            if num * 2 in number_set:
                return True
            number_set.add(num)
        return False
        