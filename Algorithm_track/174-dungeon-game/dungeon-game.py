class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        memoization = {}

        def dp(i, j):
            if i >= n or j >= m:
                return float('inf')

            if i == n - 1 and j == m - 1:
                return max(1, 1 - dungeon[i][j])

            # check memo if it is already computed
            if (i, j) in memoization:
                return memoization[(i, j)]
            
            memoization[(i, j)] = max(1, min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j]) # ggo left or right decrease the heath by dungeon value
            
            return memoization[(i, j)]

        return abs(dp(0, 0))