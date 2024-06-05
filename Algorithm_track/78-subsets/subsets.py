class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start, comb):
            result.append(comb.copy())

            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(0, [])

        return result