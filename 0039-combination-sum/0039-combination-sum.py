import copy
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        state = []
        candidates.sort()
        self.search(state, target, candidates, 0 , solutions)
        return solutions

    def is_valid_state(self, state, target):
        # check if it is a valid solution
        return sum(state) == target

    def get_candidates(self, state, target, candidates):
        if sum(state) > target:
            return []
        else:
            return candidates

    def search(self, state, target, candidates,  start, solutions):
        if self.is_valid_state(state, target):
            solutions.append(copy.deepcopy(state))
            return

        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if sum(state) + candidate > target:
                break
            state.append(candidate)
            self.search(state, target, candidates, i, solutions)
            state.pop()

    
        