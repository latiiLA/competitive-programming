class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        flag = False

        # find the number if it even exist
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            elif nums[mid] == target:
                flag = True
                i = j = mid # start the indexes to the mid
                break
        
        
        
        # Move to the left and the right until the number becomes not equal to the value
        if flag:
            while i > 0:
                if nums[i] != nums[mid]:
                    break                
                i -= 1
                
            while j < len(nums) - 1:
                if nums[j] != nums[mid]:
                    break
                j += 1

            # check if the elements at the left and the right are equal to the target if not add 1 to the index
            if nums[i] != target:
                i += 1
            if nums[j] != target:
                j -= 1

            return [i, j] 
        
        return [-1, -1]