import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        myDict = dict()

        myDict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        myList = []

        for char in digits:
            myList.append(myDict[int(char)])
        
        result = [''.join(combo) for combo in itertools.product(*myList)]

        return result



# result = [''.join(combo) for combo in itertools.product(list1, list2, list3)]
        