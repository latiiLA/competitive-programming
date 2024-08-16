class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memoization = {}
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        def dp(i, j):
            if i >= n or j >= m or obstacleGrid[i][j]:
                return 0

            if i == n - 1 and j == m - 1:
                return 1

            if (i, j) in memoization:
                return memoization[(i, j)]

            memoization[(i, j)] = dp(i + 1, j) + dp(i, j + 1) # define the recursion property. (Left and right movement) = cell as state

            return memoization[(i, j)]

        return dp(0, 0)
