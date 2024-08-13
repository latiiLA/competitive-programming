class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memoization = [[-1 for _ in range(n)] for _ in range(m)]  #matrix eclaralation
        # print(memoization)
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            #check if it is already computed
            if memoization[i][j] != -1:
                return memoization[i][j]

            memoization[i][j] = dp(i + 1, j) + dp(i, j + 1) #dp call

            return memoization[i][j]

        return dp(0, 0)

            