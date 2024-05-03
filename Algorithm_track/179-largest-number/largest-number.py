class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # change the list to a string then reverse sort, handle the case where all elements are 0
        nums = [str(element) for element in nums]
        nums.sort(key = lambda x: x * 10, reverse = True)
        
        if nums[0] == '0':
            return '0'

        return ''.join(nums)