class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0

        count = 0
        result = 0

        # check until you get more than one zero, then increase your left pointer to get the next start
        while j < n:
            if nums[j] == 0:
                count += 1
            
            while count > 1:
                if nums[i] == 0:
                    count -= 1
                i += 1
            
            result = max(result, j - i)

            j += 1

        return result