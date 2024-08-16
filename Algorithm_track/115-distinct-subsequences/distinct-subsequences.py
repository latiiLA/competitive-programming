class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        numDistinct = list(t)
        memoization = {}

        '''
            state should be the index of s and j
            recursion should have two cases. when the element of s equals t

        '''

        def dp(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0           

            if (i, j) in memoization:
                return memoization[(i, j)]

            if s[i] != t[j]:
                memoization[(i, j)] = dp(i + 1, j) # when they are not equal jump the s character
            else:
                memoization[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j) # when they are you have two option. take or not take.

            return memoization[(i, j)]

        return dp(0, 0)

