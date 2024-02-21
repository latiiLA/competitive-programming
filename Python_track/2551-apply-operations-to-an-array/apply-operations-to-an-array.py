class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # perform the operations of multiplying by 2 and making zeros
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
        # shifts zero values to the back
        i = 0
        j = 1
        while j < n:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1

        return nums

        # Acquired this solution after solving the problem with the first approach from internet

        # return sorted(nums, key=lambda x: x == 0)