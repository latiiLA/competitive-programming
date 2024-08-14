class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memoization = {}
        total = sum(nums)
        n = len(nums)
        if(total % 2 == 1):
            print("Yes")
            return 0

        def dp(i, tot):
            if total // 2 == tot: # check if they are equal sub array
                return 1
            elif i == n or tot > total // 2:
                return 0

            if (i, tot) in memoization: #(i, tot) == state
                return memoization[(i, tot)]

            memoization[(i, tot)] = dp(i + 1, tot + nums[i]) or dp(i + 1, tot) # recurrence
            return memoization[(i, tot)]

        return dp(0, 0)
