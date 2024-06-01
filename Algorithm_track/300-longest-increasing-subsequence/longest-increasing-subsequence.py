class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [nums[0]]
        def binary_search(low, high, target):
            if low > high:
                return low
            mid = (low + high)//2
            if result[mid] >= target:
                return binary_search(low, mid-1, target)
            return binary_search(mid+1, high, target)

        for i in range(1, len(nums)):
            # find the right index for nums[i] in result
            idx = binary_search(0, len(result)-1, nums[i])
            if idx == len(result):
                result.append(nums[i])
            else:
                result[idx] = nums[i]
        return len(result)   
            
