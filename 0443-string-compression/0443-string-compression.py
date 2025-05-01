from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write the compressed character
        read = 0   # Position to read the original characters
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Write the character to the array
            chars[write] = char
            write += 1

            # If the character repeats, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
