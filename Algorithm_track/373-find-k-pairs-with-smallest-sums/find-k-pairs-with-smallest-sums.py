class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        result = []
        while k > 0 and heap:
            _, n1, n2, idx = heappop(heap)

            result.append((n1, n2))
            if idx + 1 < len(nums2):
                heappush(heap, (n1 + nums2[idx + 1], n1, nums2[idx + 1], idx + 1))

            k -= 1

        return result           