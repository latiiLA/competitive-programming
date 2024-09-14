class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        summ = sum(nums)
        cnt = 0
        cnt = (target//summ)*len(nums)
        target %= summ
        nums = nums + nums

        min_len = float('inf')
        
        start = 0
        current_sum = 0    
        for end in range(len(nums)):
            current_sum += nums[end]
            while start<end and current_sum >= target:
                if current_sum == target:
                    min_len = min(min_len, end - start + 1)
                current_sum -= nums[start]
                start += 1
            if current_sum == target:
                    min_len = min(min_len, end - start + 1)

        return cnt+min_len if min_len != float('inf') else cnt if cnt and not target else -1