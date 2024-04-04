class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(nums, k):
            n = len(nums)
            i = 0

            result = 0
            dictionary = {}

            for j in range(n):
                dictionary[nums[j]] = dictionary.get(nums[j], 0) + 1             

                while len(dictionary) > k:
                    dictionary[nums[i]] -= 1
                    if dictionary[nums[i]] == 0:
                        del dictionary[nums[i]]
                    i += 1

                result += j - i + 1
            return result

        return helper(nums, k) - helper(nums, k - 1)