class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        # compares two consecutive elements of the sorted numbers if they are equal return True 
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
            