class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start, comb):
            # add if the combination length equals n
            if len(comb) == n:
                result.append(comb.copy())
            
            # start from from xero for every backtrack and leave the element that are already added to the list
            for i in range(0, n):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    backtrack(i + 1, comb)
                    comb.pop()

        backtrack(0, [])

        return result
