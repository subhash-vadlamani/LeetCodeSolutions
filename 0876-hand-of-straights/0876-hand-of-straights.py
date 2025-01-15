class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        # sort the hand list
        hand.sort()

        while hand:
            current_set = set()
            for i in range(len(hand)):
                if len(current_set) == 0:
                    current_set.add(i)
                    current_num = hand[i]
                    continue
                
                if len(current_set) == groupSize:
                    break
                
                if hand[i] == current_num + 1:
                    current_set.add(i)
                    current_num = hand[i]
            
            # print("hand - {}. current_set - {}".format(hand, current_set))
            if len(current_set) != groupSize:
                return False

            for index in sorted(current_set, reverse = True):
                hand.pop(index)
        return True
        