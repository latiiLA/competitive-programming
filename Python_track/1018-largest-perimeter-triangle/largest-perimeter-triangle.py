class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # sort and reverse the list to have it in descending order
        nums = list(reversed(sorted(nums)))

        # This is to check if three elements of the list form a triangle. the premeter will be large hence it is reverse sorted
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0