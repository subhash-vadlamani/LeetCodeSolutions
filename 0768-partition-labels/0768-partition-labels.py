class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = dict()
        for i in range(len(s)):
            last[s[i]] = i
        output = []
        size = 0
        end = 0

        for i in range(len(s)):

            if i > end:
                output.append(size)
                size = 0

            end = max(end, last[s[i]])
            size += 1
        
        output.append(size)
        return output

        