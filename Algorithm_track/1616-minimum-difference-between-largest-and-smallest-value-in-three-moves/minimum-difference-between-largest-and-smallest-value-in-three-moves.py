class Solution:
    def minDifference(self, A: List[int]) -> int:
        '''hint'''
        if len(A) < 5:
            return 0
        A.sort()
        return min(A[-1] - A[3], A[-2] - A[2], A[-3] - A[1], A[-4] - A[0])