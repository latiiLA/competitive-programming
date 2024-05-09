# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        i = 0
        j = n - 1

        while i <= j:
            mid = (i + j) // 2
            if isBadVersion(mid) == False:
                i = mid + 1
            else:
                j = mid - 1
        
        return j + 1
