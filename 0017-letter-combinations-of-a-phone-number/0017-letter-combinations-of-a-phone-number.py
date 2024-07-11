class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_mapping = dict()
        digit_mapping[2] = ["a", "b", "c"]
        digit_mapping[3] = ["d", "e", "f"]
        digit_mapping[4] = ["g", "h", "i"]
        digit_mapping[5] = ["j", "k", "l"]
        digit_mapping[6] = ["m", "n", "o"]
        digit_mapping[7] = ["p", "q", "r", "s"]
        digit_mapping[8] = ["t", "u", "v"]
        digit_mapping[9] = ["w", "x", "y", "z"]

        state = ""
        solutions = []
        digit_length = len(digits)
        self.search(state, digits, digit_length, digit_mapping, solutions)
        return solutions



    def is_valid_state(self, state, digit_length):
        # check if it is a valid solution
        if len(state) == digit_length:
            return True
        else:
            return False

    def get_candidates(self, state, digits, digit_length, digit_mapping):
        if len(state) == digit_length:
            return []
        else:
            current_state_length = len(state)
            current_digit = int(digits[current_state_length])
            current_digit_candidates = digit_mapping[current_digit]

            return current_digit_candidates

    def search(self, state, digits, digit_length, digit_mapping, solutions):
        if self.is_valid_state(state, digit_length):
            candidate = state
            solutions.append(candidate)
            return

        for candidate in self.get_candidates(state, digits, digit_length, digit_mapping):
            state += candidate
            self.search(state, digits, digit_length, digit_mapping, solutions)
            state = state[:-1]


            # state.add(candidate)
            # search(state, solutions)
            # state.remove(candidate)



        