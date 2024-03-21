class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        if k <= 1:
            return 0
        
        product = 1
        count = 0
        i = 0
        j = 0

        # Adds the product decrease i until 
        while j < n:
            product = product * nums[j]

            while i < n and product >= k:
                product /= nums[i]
                i += 1
            
            count += j - i + 1
            j += 1
            
        return count