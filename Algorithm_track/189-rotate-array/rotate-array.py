class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using the slicing method --- if the index is negative we need to take the 
        slicing_index = (len(nums) - k) % len(nums)
        
        nums[:] = nums[slicing_index:] + nums[:slicing_index]

        return nums
        