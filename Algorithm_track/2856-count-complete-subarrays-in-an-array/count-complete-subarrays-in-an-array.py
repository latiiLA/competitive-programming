class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinict = len(set(nums))

        i = 0
        j = 0

        dictionary = {}
        result = 0

        # Find the dictinict sub arrays using n - j. 
        while j < n:
            dictionary[nums[j]] = dictionary.get(nums[j], 0) + 1
            
            while len(dictionary) == distinict:
                result += n - j
                dictionary[nums[i]] -= 1
                if dictionary[nums[i]] == 0:
                    del dictionary[nums[i]]
                i += 1

            j += 1

        return result