class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Optimized solution to determine if the target triplet can be formed.
        We check for each triplet if all its elements are <= corresponding target elements,
        and if so, we use it to "cover" the target elements.
        """

        # Initialize a result triplet to track covered elements
        result = [0, 0, 0]

        # Iterate through each triplet
        for triplet in triplets:
            # If the triplet exceeds the target in any dimension, skip it
            if all(triplet[i] <= target[i] for i in range(3)):
                # Update the result to include the current triplet
                for i in range(3):
                    result[i] = max(result[i], triplet[i])

        # Check if the result matches the target
        return result == target