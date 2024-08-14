class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memoization = [[-1] * m for _ in range(n)]
        # print(memoization)

        def dp(r, c):
            if r >= n or c >= m: # boundary checker
                return float('inf')
            if r == n - 1 and c == m - 1: # base case the end cell
                return grid[r][c]

            if memoization[r][c] != -1: # return the result if it is already computed
                return memoization[r][c]
            else:
                memoization[r][c] = min(dp(r + 1, c), dp(r, c + 1)) + grid[r][c]

            return memoization[r][c]

        return dp(0, 0)

            
            
