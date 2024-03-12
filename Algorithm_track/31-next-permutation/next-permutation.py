class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        i = len(nums) - 1
        j = i - 1

        pivot = 0

        # find pivot element where the numbers starts to decrease
        while j >= 0:
            if nums[j] < nums[i]:
                pivot = i
                break
            i -= 1
            j -= 1
        
        # this means the element is reverse sorted
        if pivot == 0:
            nums[:] = nums[::-1]
            return nums
        
        swap = len(nums) - 1

        # find the numbers that is greater than the pivot
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        # swap and reverse the list from the pivot to the end
        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
        nums[pivot:] = reversed(nums[pivot:])














        # i = 0
        # j = len(nums) - 2

        # flag = True

        # # loop from the back and swap to male it greater next permutation.
        # while i >= 0:
        #     if i >= 0 and nums[j] > nums[i]:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         flag = False
        #         return

        #     else:
        #         nums[j], nums[i] = nums[i], nums[j]
            
        #     i -= 1
        #     j -= 1
        
        # # this will be executed if if statement is not executed to reverse the list
        # if flag:
        #     nums.sort()
        #     return
        