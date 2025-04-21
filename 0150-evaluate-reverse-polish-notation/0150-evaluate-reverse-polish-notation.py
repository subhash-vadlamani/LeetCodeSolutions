class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator_set = set()
        operator_set.add("+")
        operator_set.add("-")
        operator_set.add("*")
        operator_set.add("/")

        for token in tokens:
            if token not in operator_set:
                stack.append(token)
            else:
                second_number = int(stack.pop())
                first_number = int(stack.pop())

                new_number = None

                if token == "+":
                    new_number = first_number + second_number
                elif token == "-":
                    new_number = first_number - second_number
                elif token == "*":
                    new_number = first_number * second_number
                
                else:
                    new_number = int(first_number / second_number)
                stack.append(str(new_number))
        
        answer = int(stack.pop())
        return answer

        