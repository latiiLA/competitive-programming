class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)

        curr_sum = sum(nums[0:k])

        max_sum = curr_sum

        i = 1
        j = k
        
        if n == k:
            return sum(nums) / k

        while j < n:
            curr_sum = curr_sum - nums[i-1] + nums[j]
            max_sum = max(max_sum, curr_sum)            

            i += 1
            j += 1
        
        return max_sum / k
            
