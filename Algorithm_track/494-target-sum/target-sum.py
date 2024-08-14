class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memoization = {}

        def dp(i, tot):
            if i == n and tot == target:
                return 1
            elif i == n:
                return 0

            if (i, tot) in memoization:
                return memoization[(i, tot)]
            memoization[(i, tot)] = dp(i + 1, tot + nums[i]) + dp(i + 1, tot - nums[i])

            return memoization[(i, tot)]

        return dp(0, 0)
                           

            
