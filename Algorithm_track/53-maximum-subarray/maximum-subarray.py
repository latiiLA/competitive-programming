class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = []
        prefix.append(nums[0])

        j = 1

        while j < len(nums):
            prefix.append(max(nums[j], prefix[-1] + nums[j]))
            j += 1

        return max(prefix)
