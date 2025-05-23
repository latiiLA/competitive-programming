class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        if nums[0] == '0':
            return "0"

        return "".join(nums)