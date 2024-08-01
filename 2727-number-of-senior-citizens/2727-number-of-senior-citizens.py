class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorCount = 0

        for detail in details:
            currentPassengerAge = int(detail[11:13])
            if currentPassengerAge > 60:
                seniorCount += 1
        return seniorCount
        