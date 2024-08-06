class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # base case
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # memoize the dp results
        memoization = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            memoization.append(max(memoization[i - 1], memoization[i - 2] + nums[i]))

        return memoization[-1]