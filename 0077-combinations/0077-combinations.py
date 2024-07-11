class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution = []
        state = []
        self.search(state, 1, n, k, solution)
        return solution

    def is_valid_state(self, state, k):
        # check if it is a valid solution
        return len(state) == k

    def get_candidates(self, state, start, n):
        return range(start, n + 1)

    def search(self, state, start, n, k,  solution):
        if self.is_valid_state(state, k):
            solution.append(state.copy())
            return

        for candidate in self.get_candidates(state, start, n):
            state.append(candidate)
            self.search(state, candidate + 1, n, k, solution)
            state.pop()
        