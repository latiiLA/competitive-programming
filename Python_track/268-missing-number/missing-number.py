class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of all elements from 0 to n minus the sum the list to get an element that is left from the list

        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)