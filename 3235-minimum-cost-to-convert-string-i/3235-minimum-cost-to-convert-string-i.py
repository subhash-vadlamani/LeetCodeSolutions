class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        letterToNumber = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        def computeMinimumDistanceMatrix(original, changed, cost, letterToNumber):
            distanceMatrix = [[float('inf')] * 26 for _ in range(0, 26)]

            listLength = len(original)

            for i in range(0, listLength):
                currentOriginalCharacter = original[i]
                currentChangedCharacter = changed[i]
                currentChangeCost = cost[i]

                currentOriginalIndex = letterToNumber[currentOriginalCharacter]
                currentChangedIndex = letterToNumber[currentChangedCharacter]

                if currentChangeCost < distanceMatrix[currentOriginalIndex][currentChangedIndex]:
                    distanceMatrix[currentOriginalIndex][currentChangedIndex] = currentChangeCost
            
            for k in range(0, 26):
                for i in range(0, 26):
                    for j in range(0, 26):
                        if distanceMatrix[i][k] + distanceMatrix[k][j] < distanceMatrix[i][j]:
                            distanceMatrix[i][j] = distanceMatrix[i][k] + distanceMatrix[k][j]
            

            return distanceMatrix

        minimumDistanceMatrix = computeMinimumDistanceMatrix(original, changed, cost, letterToNumber)

        givenStringLength = len(source)
        finalMinimumCost = 0

        for i in range(0, givenStringLength):
            if source[i] != target[i]:
                sourceIndex = letterToNumber[source[i]]
                targetIndex = letterToNumber[target[i]]
                currentCharacterConvertCost = minimumDistanceMatrix[sourceIndex][targetIndex]
                if currentCharacterConvertCost == float('inf'):
                    return -1
                finalMinimumCost += currentCharacterConvertCost
        return finalMinimumCost


        


        