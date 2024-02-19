class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        # count if its decreasing and updates and checks if its exists before in the previous_values list
        for i in range(0, len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            
            # this checks for cases like 3  7  5
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else: # this checks for cases like 3 4 2
                nums[i + 1] = nums[i]

            changed = True

        return True            