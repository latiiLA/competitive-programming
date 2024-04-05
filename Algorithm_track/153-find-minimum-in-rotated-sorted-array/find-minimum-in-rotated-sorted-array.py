class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if nums[0] < nums[-1]:
            start = 0
        else:
            start = len(nums) - 1
        
        if start == 0:
            while nums[start] > nums[start + 1]:
                start += 1
        
        elif start == len(nums) - 1:
            while nums[start] > nums[start - 1]:
                start -= 1
        
        return nums[start]