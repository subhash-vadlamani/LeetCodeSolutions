class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        total_deficit = 0
        current_start = 0
        current_deficit = 0

        for i in range(len(diff)):
            total_deficit += diff[i]
            current_deficit += diff[i]

            if current_deficit < 0:
                current_deficit = 0
                current_start = i + 1
        
        return current_start if total_deficit >= 0 else -1
        