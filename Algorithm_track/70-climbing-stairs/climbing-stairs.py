class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        memoization = [1, 2]

        for i in range(2, n):
            memoization.append(memoization[i - 1] + memoization[i - 2])

        return memoization[-1]     
