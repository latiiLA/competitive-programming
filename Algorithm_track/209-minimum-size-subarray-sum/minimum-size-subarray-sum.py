class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i, curr_sum = 0, 0
        minimum_sum_length = float("inf")
        i = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                minimum_sum_length = min(r-i + 1, minimum_sum_length)
                curr_sum -= nums[i]
                i += 1
        
        return 0 if minimum_sum_length == float("inf") else minimum_sum_length
