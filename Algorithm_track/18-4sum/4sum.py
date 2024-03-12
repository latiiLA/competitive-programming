class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums.sort() # sort the elements

        if len(nums) < 4:
            return result

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: # remove duplicates
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: # remove duplicates
                    continue

                k = j + 1
                l = len(nums) - 1

                target2 = target - nums[i] - nums[j]

                while k < l:
                    if nums[k] + nums[l] < target2:
                        k += 1
                    elif nums[k] + nums[l] > target2:
                        l -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # removes duplicates
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return result























        # # for i in range(len(nums)):
        # #     j = i + 1

        # #     left = j + 1
        # #     right = len(nums) - 1

        # #     target2 = target - nums[i] + nums[j]

        # #     while left < len(nums) and sumation < target2:
        # #         if nums[left] + nums[right] < target






































        # '''
        # # pointer for the first loop at the beginning and at the end
        # i = 0
        # j = len(nums) - 1

        # result = []

        # # Take the first and last element then check if there exists two numbers in between those numbers that equals the target
        # while i < j:
        #     left = i + 1
        #     right = j - 1

        #     temporary = nums[i] + nums[j] + nums[left] + nums[right]

        #     target2 = target - nums[i] - nums[j]
            
        #         # Second loop to check from the second and third pointers
        #     while left < right:
        #         temp = nums[left] + nums[right]

        #         if temp < target2:
        #             left += 1
        #         elif temp > target2:
        #             right -= 1
        #         else:
        #             # jump if there exists the solution in the result array
        #             if len(result) > 0 and [nums[i], nums[j], nums[left], nums[right]] == result[-1]:
        #                 left += 1
        #                 # right -= 1
        #                 continue
        #             else:
        #                 result.append([nums[i], nums[left], nums[right], nums[j]])
        #                 left += 1
        #                 # right -= 1

            
        #     # this checks where the first loop should decrease to or increase to based on its comparison with the target
        #     if temporary > target:
        #         j -= 1
        #     elif temporary < target:
        #         i += 1
        #     else:
        #         i += 1
        #         j -= 1

        # return result
        # '''

                

            


















        # # print(nums)

        # # count = 0

        # # i = 0
        # # j = 1
        # # while j < len(nums):
        # #     if nums[i] != nums[j]:

        # #         left = i + 2

        # #         right = left + 1

        # #         while right < len(nums):
        # #             if nums[i] + nums[j] + nums[left] + nums[right] == target:
        # #                 result.append([nums[i], nums[j], nums[left], nums[right]])
                    
        # #             left += 1
        # #             right += 1
                
        # #         count = 0
        # #         i += 1
        #         j += 1
        #     elif nums[i] == nums[j] and count == 0:

        #         # if nums[i] != nums[j]:

        #         left = i + 2

        #         right = left + 1

        #         while right < len(nums):
        #             if nums[i] + nums[j] + nums[left] + nums[right] == target:
        #                 result.append([nums[i], nums[j], nums[left], nums[right]])
                    
        #             left += 1
        #             right += 1
                
        #         count = 0
        #         i += 1
        #         j += 1

            
        #     elif nums[i] == nums[j] and count > 0:
        #         i += 1
        #         j += 1
            
