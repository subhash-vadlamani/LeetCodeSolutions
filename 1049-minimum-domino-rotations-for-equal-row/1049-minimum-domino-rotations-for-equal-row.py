from collections import defaultdict
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
            maintain a dict
            key is the number on the face
            value is the set containing the index of the dominos containing that
        """

        required_set = set(range(len(tops)))
        top_dict = defaultdict(set)
        bottom_dict = defaultdict(set)

        for i in range(len(tops)):
            top_dict[tops[i]].add(i)
        
        for i in range(len(bottoms)):
            bottom_dict[bottoms[i]].add(i)
        

        minimum_rotations_required = float('inf')
        for i in range(1, 7):
            current_top_indices_set = set()
            current_bottom_indices_set = set()

            if i in top_dict:
                current_top_indices_set = top_dict[i]
            
            if i in bottom_dict:
                current_bottom_indices_set = bottom_dict[i]
            
            if required_set == current_top_indices_set | current_bottom_indices_set:
                print(f"for {i} number, top_set is {current_top_indices_set}, bottom_set is {current_bottom_indices_set}")
                minimum_rotations_required = min(minimum_rotations_required, min(len(current_top_indices_set), len(current_bottom_indices_set)) - len(current_top_indices_set & current_bottom_indices_set))
        

        return minimum_rotations_required if minimum_rotations_required != float('inf') else -1
            


        