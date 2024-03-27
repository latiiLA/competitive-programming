class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        result = [1] * len(nums)

        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]
            suffix[i + 1] = suffix[i] * nums[n - i - 1]

        print(prefix, suffix)
        
        for i in range(n):
            print(prefix[i], suffix[n - i])
            result[i] = prefix[i] * suffix[n - i - 1]
        
        return result
            
        
        
        
        
        
        
        
        # answer = [1] * len(nums)
        # prefix = 1
        # postfix = 1

        # for i in range(len(nums)):
        #     answer[i] = prefix
        #     prefix *= nums[i]

        # for i in range(len(nums)-1, -1, -1):
        #     answer[i] *= postfix
        #     postfix *= nums[i]

        # return answer            