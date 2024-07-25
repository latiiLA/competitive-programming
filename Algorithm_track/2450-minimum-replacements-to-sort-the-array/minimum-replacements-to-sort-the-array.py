class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[-1]
        splits = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > last:
                split_parts = ceil(nums[i] / last)
                splits += split_parts - 1
                last = nums[i] // split_parts
            else:
                last = nums[i]

        return splits