class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        i = 0
        sum_ = 0
        result = float('-inf')
        total = sum(nums)
        target = total - x
        
        if total < x:
            return -1

        # Hint helped -- find the longest value that is equal to the total - target value
        for j in range(n):
            sum_ += nums[j]
            while sum_ > target:
                sum_ -= nums[i]
                i += 1

            if sum_ == target:
                result = max(result, j - i + 1)
            
            j += 1

        return -1 if result == float('-inf') else n - result
