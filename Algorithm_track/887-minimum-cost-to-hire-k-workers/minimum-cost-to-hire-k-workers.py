import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        
        workers = []
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        
        workers.sort()
        
        total_quality = 0
        max_heap = []
        min_cost = float('inf')
        
        # Iterate over the sorted workers
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                cost = total_quality * ratio
                min_cost = min(min_cost, cost)
        
        return min_cost
