class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) 
        left = 0
        right = n - 1

        # Try to find the index that makes the length the value of value = n - index
        while left <= right:
            mid = (left + right) // 2

            if citations[mid] > n - mid:
                right = mid - 1
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                return citations[mid]

        return n - left
        
            