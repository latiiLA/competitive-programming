class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes + numZeros >= k: # if the numOnes is greater than or equal to k we take that else we will take k
            return min(numOnes, k)
        else:
            total = numOnes + numZeros
            decrease = k - total
            return numOnes - decrease         