class Solution:
    def numTeams(self, rating: List[int]) -> int:

        answerCount = 0
        ratingLength = len(rating)

        smallerDict1 = dict()
        smallerDict2 = dict()
        biggerDict1 = dict()
        biggerDict2 = dict()

        for i in range(0, ratingLength):
            currentElement = rating[i]
            smallerDict1[currentElement] = []
            smallerDict2[currentElement] = []
            biggerDict1[currentElement] = []
            biggerDict2[currentElement] = []

            for j in range(i-1, -1, -1):
                if rating[j] < currentElement:
                    smallerDict1[currentElement].append(rating[j])
                else:
                    biggerDict2[currentElement].append(rating[j])

            for j in range(i+1, ratingLength):
                if rating[j] > currentElement:
                    biggerDict1[currentElement].append(rating[j])
                else:
                    smallerDict2[currentElement].append(rating[j])

        
        for i in range(0, ratingLength):
            middleElement = rating[i]
            answerCount += (len(smallerDict1[middleElement]) * len(biggerDict1[middleElement])) + (len(smallerDict2[middleElement]) * len(biggerDict2[middleElement]))
            # numberLowerElements = len(smallerDict[middleElement])
            # numberUpperElements = len(biggerDict[middleElement])
            # currentElementCombinations = numberLowerElements * numberUpperElements

            # answerCount += currentElementCombinations
        return answerCount



        # for i in range(0, ratingLength):
        #     for j in range(i+1, ratingLength):
        #         for k in range(j+1, ratingLength):
        #             if (rating[i] < rating[j]) and (rating[j] < rating[k]):
        #                 answerCount += 1
        #                 continue
        #             if (rating[i] > rating[j]) and (rating[j] > rating[k]):
        #                 answerCount += 1
        # return answerCount

        