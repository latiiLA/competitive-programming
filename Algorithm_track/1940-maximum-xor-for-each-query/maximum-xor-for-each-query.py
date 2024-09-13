class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        prefix_sum = [nums[0]]
        for a in range(1, len(nums)):
            prefix_sum.append(prefix_sum[len(prefix_sum)-1] ^ nums[a])
       
        comparison = 2 ** maximumBit
        ans = []
        #for each query
        for i in range(len(prefix_sum)-1, -1, -1):
            #get the res so far!
            current_res = prefix_sum[i]
            res = current_res ^ (comparison - 1)
            ans.append(res)
        return ans