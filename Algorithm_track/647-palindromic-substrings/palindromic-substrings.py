class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp approach

        n = len(s)
        memo = {}

        # dp definition --- check from outer to inside until we end looking at all elements or get non palindromic combination
        def dp(i, j):
            if i >= j:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = dp(i+1, j - 1)
            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        # check for all palindrome combinations
        # takes n ** 2 time comp. 
        result = 0
        for i in range(n):
            for j in range(i, n):
                result += dp(i, j)

        return result