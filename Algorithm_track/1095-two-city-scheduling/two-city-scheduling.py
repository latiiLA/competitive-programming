class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = []
        minimum_cost = 0

        # capture the difference in distance in 
        for city in costs:
            diff.append((city[0] - city[1], city[0], city[1]))

        diff.sort() # sort the difference

        # take the first half for city 'a' because that gives you the minimum distance
        for i in range(n // 2):
            minimum_cost += diff[i][1]
        
        # take the second half for city 'b' because that gives you the minimum distance for city b 
        # --hence the sort to get the minimum for city 'a' the second half will the best sort you can get for city b
        for i in range(n // 2, n):
            minimum_cost += diff[i][2]

        return minimum_cost