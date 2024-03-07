class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []

        encountedSum = {}

        i = 0 # first pointer

        while i < len(nums):
            target = 0 - nums[i] # this is the target number we are looking for the two sum
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue


            # two sum created from the 3Sum problem
            while left < right:
                temp = nums[left] + nums[right]
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    tempList = [nums[i], nums[left], nums[right]]
                    result.append(tempList)

                    # this removes if the consecutive numbers are equal to remove the duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                
            i += 1

        return result