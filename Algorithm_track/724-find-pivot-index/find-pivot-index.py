class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = sum(nums)

        # Find prefix and suffix by increasing and decreasing precalculated values of them
        for i in range(n):
            if prefix == suffix - nums[i]:
                return i
            
            prefix += nums[i]
            suffix -= nums[i]

        return -1