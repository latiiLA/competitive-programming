class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        index = 0
        
        i = 0

        j = 1

        while i < len(nums):
            count = 0
            if j < len(nums) and nums[i] != nums[j]:
                nums[index] = nums[i]
                index += 1
                i += 1
                j += 1
            elif i == len(nums) - 1:
                nums[index] = nums[i]
                index += 1
                break
            else:
                while j < len(nums) and nums[i] == nums[j]:
                    
                    if count < 2:
                        nums[index] = nums[i]
                        index += 1
                        nums[index] = nums[j]
                        index += 1
                        count = 2
                    else:
                        j += 1

                i = j
                j = j + 1

        return len(nums[:index])