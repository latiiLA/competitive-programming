class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}

        # Loop through the list and updates and searchs the dictionary for elements in list until the target is attained
        for i, num in enumerate(nums):
            if num in two_sum:
                return [two_sum[num], i]
            two_sum[target - num] = i           
