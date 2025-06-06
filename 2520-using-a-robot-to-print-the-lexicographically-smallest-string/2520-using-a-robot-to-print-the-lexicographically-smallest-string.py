from collections import OrderedDict, deque
import string
class Solution:
    def robotWithString(self, s: str) -> str:
        """
            we have to apply one of the 2 given operations until both the strings are empty

            we can remove the first character of string s(queue?)
            we can remove the last character of string t(stack?)

            simple sorting of the string does not work(check example 3)

            first iterate the string s and store the char count in ordered dict?

            while queue is still non empty, keep searching for the lexicographically
            smallest characters by iterating over the ordered dict. Once the queue is empty,
            pop the stack completly
        """

        def count_letters_ordered(s):
            od = OrderedDict((char, 0) for char in string.ascii_lowercase)

            for ch in s:
                if ch in od:
                    od[ch] += 1
            return od
        
        letter_counts = count_letters_ordered(s)
        my_queue = deque()
        for ch in s:
            my_queue.append(ch)
        my_stack = [] # stack

        answer_list = [] # list that hold the characters in the lexicographically smallest order possible

        min_char = 'a'

        while my_queue:

            ch = my_queue.popleft()
            my_stack.append(ch)
            letter_counts[ch] -= 1

            while min_char <= 'z' and letter_counts[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            while my_stack and my_stack[-1] <= min_char:
                answer_list.append(my_stack.pop())
        
        while my_stack:
            answer_list.append(my_stack.pop())
        
        return "".join(answer_list)
        