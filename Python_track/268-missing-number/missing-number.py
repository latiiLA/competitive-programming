class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums) + 1):
            print(num)
            if not num in nums:
                return num