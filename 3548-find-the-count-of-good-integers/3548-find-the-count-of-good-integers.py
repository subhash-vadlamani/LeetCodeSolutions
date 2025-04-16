class Solution:
    def __init__(self):
        self.k_palindromes = 0
        self.done = set()
        self.fact = [0] * 11

    def precompute_factorial(self, n):
        self.fact[0] = 1
        self.fact[1] = 1
        for i in range(2, 11):
            self.fact[i] = i * self.fact[i - 1]

    def count_all_permutations(self, freq, n):
        count = self.fact[n]
        for i in range(10):
            count //= self.fact[freq[i]]
        return count

    def all_arrangements(self, number, n):
        sorted_num = ''.join(sorted(number))
        num = int(sorted_num)
        if num in self.done:
            return 0

        self.done.add(num)
        freq = [0] * 10
        for c in sorted_num:
            freq[int(c)] += 1

        total_permutations = self.count_all_permutations(freq, n)
        invalid_permutations = 0
        if freq[0] > 0:
            freq[0] -= 1
            invalid_permutations = self.count_all_permutations(freq, n - 1)
        return total_permutations - invalid_permutations

    def is_k_palindrome(self, number, n, k):
        return int(number) % k == 0

    def generate_palindromes(self, pos, n, number, k):
        if pos >= (n + 1) // 2:
            num_str = ''.join(number)
            if self.is_k_palindrome(num_str, n, k):
                self.k_palindromes += self.all_arrangements(num_str, n)
            return

        start = '1' if pos == 0 else '0'
        for c in range(ord(start), ord('9') + 1):
            number[pos] = chr(c)
            number[n - pos - 1] = chr(c)
            self.generate_palindromes(pos + 1, n, number, k)
        number[pos] = ' ' 

    def countGoodIntegers(self, n: int, k: int) -> int:
        self.precompute_factorial(n)
        number = [' '] * n
        self.generate_palindromes(0, n, number, k)
        return self.k_palindromes 