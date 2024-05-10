class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # Calculate mid and compare it with the first or last element of the array to make the movement
        while left <= right:
            mid = (left + right) // 2

            # if nums[mid + 1] < nums[mid]:
            #     return nums[mid + 1]
            # elif nums[mid - 1] < nums[mid]:
            #     return nums[mid - 1]
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
            
        return nums[left]
