class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                answer = [i + 1, j + 1]
                return answer
                break
            elif current_sum  < target:
                i += 1
            else:
                j -= 1
        

            
        