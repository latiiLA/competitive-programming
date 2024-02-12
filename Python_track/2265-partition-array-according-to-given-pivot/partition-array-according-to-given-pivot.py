class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less_than_pivot = []
        greater_than_pivot = []
        pivots = []

        # Loop through the array and sidentify elements less than and greater than the pivot
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                pivots.append(num)

        print(less_than_pivot, greater_than_pivot)

        less_than_pivot = less_than_pivot + pivots + greater_than_pivot

        return less_than_pivot