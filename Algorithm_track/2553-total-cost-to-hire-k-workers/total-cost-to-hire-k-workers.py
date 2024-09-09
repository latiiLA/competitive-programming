class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        counts = Counter(costs) # helps us to remove remove duplicate elements we have used for one one of the heap, to be removed on the second heap
        # create two left and right heap as mentioned on the hint
        leftCost = []
        rightCost = []
        
        i = 0
        while i < candidates:
            heappush(leftCost, costs[i])
            i += 1
        
        j = n - 1
        while j > n - candidates - 1:
            heappush(rightCost, costs[j])
            j -= 1
        
        # print(leftCost, rightCost, i, j)
        totalCost = 0

        # take the minimum of the two heaps and add new element if you costs array is not empty to maintain the k heap size
        while i <= j or k > 0:
            while leftCost and counts[leftCost[0]] == 0:
                heappop(leftCost)
                if i <= j:
                    heappush(rightCost, costs[i])
                    i += 1
            while rightCost and counts[rightCost[0]] == 0:
                heappop(rightCost)
                if i <= j:
                    heappush(leftCost, costs[j])
                    j -= 1

            if not rightCost or (leftCost and leftCost[0] <= rightCost[0]):
                if counts[leftCost[0]] > 0:
                    counts[leftCost[0]] -= 1
                totalCost += heappop(leftCost)
                if i <= j:
                    heappush(leftCost, costs[i])
                    i += 1
            else:
                if counts[rightCost[0]] > 0:
                    counts[rightCost[0]] -= 1
                
                totalCost += heappop(rightCost)
                if i <= j:
                    heappush(rightCost, costs[j])
                    j -= 1

            # print(leftCost, rightCost, totalCost)
            k -= 1
            if k == 0:
                break            

        return totalCost