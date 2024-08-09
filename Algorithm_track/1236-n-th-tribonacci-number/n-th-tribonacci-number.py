class Solution:
    
    def tribonacci(self, n: int) -> int:
        memoization = {}
        def dp(n):
            if n < 2:
                return n

            elif n == 2:
                return 1

            # This is top down approach --- this can also be solved by bottom up appraoch reducing the backtracking
            if n not in memoization:
                memoization[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)

            return memoization[n]

        return dp(n)        