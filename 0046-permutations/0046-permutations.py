import copy
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        state = []
        nums_length = len(nums)
        number_set = set(nums)
        self.search(state, nums_length, number_set, solutions)
        return solutions

    def is_valid_state(self, state, nums_length):
        # check if it is a valid solution
        return len(state) == nums_length

    def get_candidates(self, state, number_set):
        candidate_set = number_set.copy()
        for element in state:
            candidate_set.remove(element)
        return list(candidate_set)

    def search(self, state, nums_length, number_set, solutions):
        if self.is_valid_state(state, nums_length):
            solutions.append(copy.deepcopy(state))
            return

        for candidate in self.get_candidates(state, number_set):
            state.append(candidate)
            self.search(state, nums_length, number_set, solutions)
            state.pop()


    
        