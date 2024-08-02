class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        repeatingSubstringFound = False
        stringLength = len(s)

        currentSubstringLength = len(s) - 1
        i = 0
        j = i + (currentSubstringLength - 1)

        while True:
            currentLengthSubstringSet = set()
            temp_i = i
            temp_j = j
            while temp_j < stringLength:
                currentSubstring = s[temp_i:temp_j+1]
                if currentSubstring not in currentLengthSubstringSet:
                    currentLengthSubstringSet.add(currentSubstring)
                else:
                    repeatingSubstringFound = True
                    break
                temp_i += 1
                temp_j += 1
            
            if repeatingSubstringFound:
                break
            currentSubstringLength -= 1
            if currentSubstringLength <= 1:
                return 0
            i = 0
            j = i + (currentSubstringLength - 1)
            
        
        return currentSubstringLength


        