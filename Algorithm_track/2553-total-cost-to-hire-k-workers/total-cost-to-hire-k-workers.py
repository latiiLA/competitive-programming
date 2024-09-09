class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        # create two left and right heap as mentioned on the hint
        leftCost = []
        rightCost = []
        
        i = 0
        while i < candidates:
            heappush(leftCost, costs[i])
            i += 1
        
        j = n - 1
        while j > max(candidates - 1, n - candidates - 1):
            heappush(rightCost, costs[j])
            j -= 1

        j = n - candidates - 1
        
        # print(costs, leftCost, rightCost, i, j)
        totalCost = 0

        # take the minimum of the two heaps
        # add new element if you costs array is not empty to maintain the k heap size
        for _ in range(k):
            if not rightCost or leftCost and leftCost[0] <= rightCost[0]:
                totalCost += heappop(leftCost)
                if i <= j:
                    heappush(leftCost, costs[i])
                    i += 1
            else:                
                totalCost += heappop(rightCost)
                if i <= j:
                    heappush(rightCost, costs[j])
                    j -= 1

            # print(leftCost, rightCost, totalCost)

        return totalCost