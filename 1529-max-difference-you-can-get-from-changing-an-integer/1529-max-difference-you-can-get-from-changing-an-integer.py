class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Find max by replacing first non-9 digit with 9
        for ch in num_str:
            if ch != '9':
                max_replace = ch
                break
        else:
            max_replace = None

        if max_replace:
            max_num = int(num_str.replace(max_replace, '9'))
        else:
            max_num = num  # already max

        # Find min by replacing first digit > 1 with 1
        for i, ch in enumerate(num_str):
            if i == 0 and ch != '1':
                min_replace = ch
                break
            elif i > 0 and ch != '0' and ch != '1':
                min_replace = ch
                break
        else:
            min_replace = None

        if min_replace:
            min_num = int(num_str.replace(min_replace, '1' if i == 0 else '0'))
        else:
            min_num = num  # already min

        return max_num - min_num
