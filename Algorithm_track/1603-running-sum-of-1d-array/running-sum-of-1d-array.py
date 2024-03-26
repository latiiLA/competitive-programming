class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [nums[0]]

        for i in range(1, n):
            result.append(result[i - 1] + nums[i])

        return result   