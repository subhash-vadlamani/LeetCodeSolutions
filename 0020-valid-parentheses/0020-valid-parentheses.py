class Solution:
    def isValid(self, s: str) -> bool:
        character_stack = []

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                character_stack.append(s[i])
            elif character_stack and ((s[i] == ')' and character_stack.pop() == '(') or (s[i] == ']' and character_stack.pop() == '[') or (s[i] == '}' and character_stack.pop() == '{')):
                continue
            else:
                return False
        if len(character_stack):
            return False
        else:
            return True