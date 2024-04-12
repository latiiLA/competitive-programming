class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        maximum_sum = 0
        n = len(nums)
        i = 0
        j = 0

        dictionary = {}
        current = 0

        for j in range(n):
            
            dictionary[nums[j]] = dictionary.get(nums[j], 0) + 1
            current += nums[j]

            while dictionary[nums[j]] > 1:
                current -= nums[i]
                dictionary[nums[i]] -= 1
                if dictionary[nums[i]] == 0:
                    del dictionary[nums[i]]
                i += 1
                           
            maximum_sum = max(maximum_sum, current)

        return maximum_sum
