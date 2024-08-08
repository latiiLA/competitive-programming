class Solution:
    def fib(self, n: int) -> int:
        memo = {} #memo

        def dp(n: int) -> int:
            if n < 2:
                return n
            if n not in memo:
                memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]  # Return the memoized value

        return dp(n)
