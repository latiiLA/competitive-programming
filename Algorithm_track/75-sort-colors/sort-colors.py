class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        result = [0] * (max(nums) + 1) # creating a list to count the elements with the range of the array

        # result of the elements
        for i in range(len(nums)):
            result[nums[i]] += 1

        # append the elements to the nums
        # nums.clear()
        k = 0
        for i in range(len(result)):
            for j in range(result[i]):
                nums[k] = i
                k += 1
        