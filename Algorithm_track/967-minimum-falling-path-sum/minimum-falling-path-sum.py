class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memoization = {}

        def dp(i, j):
            if j < 0 or j >= n: return float('inf') # check boundary. if the boundary passed return infinity bc we are finding minimum
            if i == n - 1:
                return matrix[i][j]    # We have got the the needed sub problems answer at this point so return

            if (i, j) in memoization:
                return memoization[(i, j)]
            
            memoization[(i, j)] = matrix[i][j] + min(dp(i + 1, j - 1), dp(i + 1, j), dp(i + 1, j + 1))

            return memoization[(i, j)]

        # loop through the first row to get every starting points and call dp
        ans = float('inf')
        for j in range(m):
            ans = min(ans, dp(0, j))
        
        return ans