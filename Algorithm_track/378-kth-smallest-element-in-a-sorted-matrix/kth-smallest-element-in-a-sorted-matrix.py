class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        n = len(matrix)
        m = len(matrix[0])

        # Build n**2 - k min Heap and return it. 
        # This way you wil remove k - 1 smallest element from the heap and you will be left the smallest
        for i in range(n):
            for j in range(m):
                heappush(minHeap, -matrix[i][j])

                if len(minHeap) > k and minHeap:
                    heappop(minHeap)

        return -minHeap[0]