class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # count = 0
        # # Finding the number of good pairs 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        
        # return count
        
        nums_counter = Counter(nums)
        counter = 0
        for count in nums_counter.values():
            if count > 1:
                counter += (count * (count-1) // 2)

        return counter
                        
