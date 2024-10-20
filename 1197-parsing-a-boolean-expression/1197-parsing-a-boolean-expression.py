class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "t":
            return True
        elif expression == "f":
            return False
        elif expression[0] == '!' and (expression[2] == 't' or expression[2] == 'f'):
            if expression[2] == 't':
                return False
            elif expression[2] == 'f':
                return True
        elif expression[0] == '&' and (expression[2] == 't' or expression[2] == 'f'):
            if expression[2] == 't':
                current_answer = True
            elif expression[2] == 'f':
                current_answer = False
                return current_answer
            
            expression_length = len(expression)
            for i in range(4, expression_length - 1):
                current_character = expression[i]
                if current_character == ',':
                    continue
                elif current_character == 't':
                    current_answer = current_answer & True
                elif current_character == 'f':
                    current_answer = current_answer & False
                    return current_answer
            return current_answer
        elif expression[0] == '|' and (expression[2] == 't' or expression[2] == 'f'):
            if expression[2] == 't':
                current_answer = True
                return current_answer
            elif expression[2] == 'f':
                current_answer = False
            
            expression_length = len(expression)
            for i in range(4, expression_length - 1):
                current_character = expression[i]
                if current_character == ',':
                    continue
                elif current_character == 't':
                    current_answer = current_answer | True
                    return current_answer
                elif current_character == 'f':
                    current_answer = current_answer | False
            return current_answer
        stack = []
        for char in expression:
            # if char == ',':
            #     continue
            if char != ')':
                stack.append(char)
            if char == ')':
                sub_expression = "("
                while stack:
                    top_element = stack[-1]

                    if top_element == '(':
                        stack.pop()
                        sub_expression += ")"
                        break
                    else:
                        popped_element = stack.pop()
                        sub_expression += str(popped_element)
                
                current_operation = stack.pop()
                sub_expression = str(current_operation) + sub_expression
                sub_expression_answer = self.parseBoolExpr(sub_expression)
                if sub_expression_answer:
                    stack.append('t')
                else:
                    stack.append('f')
        
        final_character = stack[0]
        if final_character == 't':
            return True
        else:
            return False
            

            

            


        