import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        state = ["", 0]
        self.search(state, n, solutions)
        return solutions

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state[0]) == 2 * n and state[1] == 0

    def get_candidates(self, state, n):
        if len(state[0]) == 2 * n:
            return []
        
        if state[1] == 0:
            return ["("]
        elif state[1] == n:
            return [")"]
        else:
            return ["(", ")"]
        

    def search(self, state, n, solutions):
        if self.is_valid_state(state, n):
            solutions.append(copy.deepcopy(state[0]))
            return

        for candidate in self.get_candidates(state, n):
            if candidate == "(":
                state[0] += "("
                state[1] += 1
            else:
                state[0] += ")"
                state[1] -= 1
            self.search(state, n, solutions)

            if candidate == "(":
                state[0] = state[0][:-1]
                state[1] -= 1
            else:
                state[0] = state[0][:-1]
                state[1] += 1

            
            # state.add(candidate)
            # search(state, solutions)
            # state.remove(candidate)

        