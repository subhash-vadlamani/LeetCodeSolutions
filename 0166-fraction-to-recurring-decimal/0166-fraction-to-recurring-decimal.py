class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # If either one is negative (not both)
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Add the integral part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(result)

        result.append('.')

        # Dictionary to store remainder positions
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, '(')
                result.append(')')
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(result)

            