class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * (1001)
        
        # perform prefix of the trips
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]

        if prefix[0] > capacity:
            return 0

        # calculate sum of the prefix at a given index and check if it is greater than the capacity
        for i in range(1, 1001):
            prefix[i] = prefix[i - 1] + prefix[i]
            if prefix[i] > capacity:
                return 0
        
        return 1