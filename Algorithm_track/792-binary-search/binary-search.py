class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        # Solve it 
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            elif nums[mid] == target:
                return mid
        
        return -1  