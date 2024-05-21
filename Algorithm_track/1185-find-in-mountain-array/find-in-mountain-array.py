# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak
        def findPeak(arr, length):
            # initialize the pointers to be one element from the beginning and one elemenent to from the end
            left = 1
            right = length - 2

            while left <= right:
                mid = (left + right) // 2
                if arr.get(mid-1) < arr.get(mid) < arr.get(mid+1):
                    left = mid + 1
                elif arr.get(mid-1) > arr.get(mid) > arr.get(mid+1):
                    right = mid - 1
                else:
                    return mid

        # search through the left array first and to the left the array
        def findElementLeft(arr, peak):
            left = 0
            right = peak
        
            while left <= right:
                mid = (left + right) // 2
                if arr.get(mid) < target:
                    left = mid + 1
                elif arr.get(mid) > target:
                    right = mid - 1
                elif arr.get(mid) == target:
                    return mid

            return -1
        
        # function to search to the array of the array
        def findElementRight(arr, peak, length):
            left = peak
            right = length - 1

            while left <= right:
                mid = (left + right) // 2
                if arr.get(mid) < target:
                    right = mid - 1
                elif arr.get(mid) > target:
                    left = mid + 1
                elif arr.get(mid) == target:
                    return mid
                
            return -1

        length = mountain_arr.length() # Get the length of the array
        peak = findPeak(mountain_arr, length) # get the peak of the array using binary search
        result = findElementLeft(mountain_arr, peak) # find the result to the left peak of the element
        if result == -1:
            result = findElementRight(mountain_arr, peak, length) # if there is no result from the left array search the to the right og the peak
        
        return result