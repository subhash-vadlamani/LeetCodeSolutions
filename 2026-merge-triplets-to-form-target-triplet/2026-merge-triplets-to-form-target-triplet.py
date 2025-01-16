class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # Greedy
        """
            I am going to iterate over individual elements of the target list.
            for that element(say 'a'), I am going to delete all the triplets
            that have the element in that place greater than 'a'.

            After doing this for all the elements in the target, if there remain any triplets,
            I will return True. Else, False.
        """

        for i in range(len(target)):
            current_target_number = target[i]
            for j in range(len(triplets) - 1, -1, -1):
                if triplets[j][i] > current_target_number:
                    triplets.pop(j)
        
        for i in range(len(target)):
            current_target_number = target[i]
            number_found = False
            for j in range(len(triplets)):
                if triplets[j][i] == current_target_number:
                    number_found = True
                    break
            if not number_found:
                return False
        return True
                
        
        