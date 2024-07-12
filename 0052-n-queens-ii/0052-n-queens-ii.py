import copy
class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = []
        state = []

        self.search(state, solutions, n)
        return len(solutions)

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        position = len(state)
        candidates = set(range(0, n))

        for row, col in enumerate(state):
            candidates.discard(col)

            dist = position - row

            candidates.discard(col + dist)
            candidates.discard(col - dist)

        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            solutions.append(copy.deepcopy(state))
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    


        