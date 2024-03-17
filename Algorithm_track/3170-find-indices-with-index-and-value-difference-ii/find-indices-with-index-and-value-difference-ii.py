class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        min_index = 0
        max_index = 0

        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[min_index]:
                min_index = i - indexDifference
            if nums[i - indexDifference] > nums[max_index]:
                max_index = i - indexDifference

            if abs(nums[i] - nums[min_index]) >= valueDifference:
                return [min_index, i]
            if abs(nums[i] - nums[max_index]) >= valueDifference:
                return [max_index, i]
            
        return [-1, -1]


        # n = len(nums)
        # result = []

        # i = indexDifference * 2
        # j = 3
        # if indexDifference == 0:
        #     return [0, 0]

        # minimum = min(nums[:indexDifference+1])
        # # print(nums[:i])
        # maximum = max(nums[:indexDifference+1])
        # # print(nums[:i])



        # while i < n:
        #     j = 0
        #     # while j <= i - indexDifference:
        #     # print(j, i - indexDifference + 1)
        #     while j < i:
        #         minimum = min(minimum, nums[j])
        #         maximum = max(maximum, nums[j])
        #         j+= 1

        #     # max_ = float("-inf")
        #     # max_index = 0
        #     # min_ = float("inf")
        #     # min_index = 0

        #     # while j < i - indexDifference + 2:
        #     #     if nums[j] <= min_:
        #     #         min_ = nums[j] 
        #     #         min_index = j
        #     #     if nums[j] >= max_:
        #     #         max_ = nums[j] 
        #     #         max_index = j

        #     #     # print(nums[j])
        #     #     # print(min_index, max_index,min_, max_)
                
        #     #     j+=1
            
        #     # print(min_, max_)
        #     # print(min_index, max_index)


        #     # print(nums[j : i - indexDifference + 2], min_, max_)
        #     if abs(nums[i] - minimum) >= valueDifference or abs(nums[i] - maximum) >= valueDifference:
        #         result.append(nums.index(minimum))
        #         result.append(i)
        #         return result
                
        #     i += 1
        
        # return [-1, -1]

















        # result = []

        # i = indexDifference
        # # i = 0

        # # # check if the condition satisfies for every element i. 
        # while i < len(nums):
        #     # j1 = j + indexDifference
        #     # while j2 < len(nums):
        #     if i - indexDifference >= indexDifference:
        #         max_ = max(nums[i - indexDifference], i + 1)
        #         min_ = min(nums[i - indexDifference], i + 1)

        #         # print(max_, min_)


        #         if abs(max_ - nums[i]) >= valueDifference:
        #             result.append(i)
        #             result.append(nums.index(max_))
        #             return result
        #         elif abs(min_ - nums[i]) >= valueDifference:
        #             result.append(i)
        #             result.append(nums.index(min_))
        #             return result
        #     else:
        #         k = i
        #         while k < len(nums):
        #             if abs(nums[k] - nums[k - indexDifference]) >= valueDifference:
        #                 result.append(k - indexDifference)
        #                 result.append(k)
        #                 return result
        #             elif abs(nums[k] - nums[i - indexDifference]) >= valueDifference:
        #                 result.append(k - indexDifference)
        #                 result.append(k)
                        
        #                 return result

        #             k += 1

        #             print(k - indexDifference, k)

                
        #     # j1 += 1

        #     # i += 1
        #     i += 1

        # # for i in range(len(nums) - indexDifference):
        # #     for j2 in range(i + indexDifference, len(nums)):
        # #         if abs(nums[j2] - nums[i]) >= valueDifference:
        # #             return [i, j2]
        # # return [-1, -1]

        # return [-1, -1]
