class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        i = 0
        mountain = 0

        count = 0
        n = len(arr)

        while i < n:
            while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1
            
            j = i + 1

            while j < n - 1 and arr[j] < arr[j + 1]:
                j += 1
            
            while j < n - 1 and arr[j] > arr[j + 1]:
                j += 1
                mountain = max(mountain, j - i + 1)

            i = j

        return mountain