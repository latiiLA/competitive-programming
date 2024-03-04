class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        targetElemIndices = []

        # return the indices of target element
        for i, num in enumerate(nums):
            if num == target:
                targetElemIndices.append(i)
            elif num > target:
                break
        
        return targetElemIndices
