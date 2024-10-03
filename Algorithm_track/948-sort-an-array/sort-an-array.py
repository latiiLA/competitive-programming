class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minHeap = []

        for num in nums:
            heappush(minHeap, num)

        result = []
        while minHeap:
            result.append(heappop(minHeap))

        return result