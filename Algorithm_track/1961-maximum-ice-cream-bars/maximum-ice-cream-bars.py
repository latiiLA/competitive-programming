class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        count = 0
        result = 0
        maximum = max(costs) + 1

        # this to sort as the question suggests using counting sort
        counting_sort = [0] * (maximum)

        for i in range(n):
            counting_sort[costs[i]] += 1
        
        print(counting_sort)
        
        # loop until the cost reaches the coins and break. in the mean time add the number of counts to our result
        for i in range(1, maximum):
            if counting_sort[i] == 0:
                continue
            result += i * counting_sort[i]
            if result <= coins:
                count += counting_sort[i]
            else:
                break
            print(result, count, i)
        
        if result > coins:
            result -= i * counting_sort[i]
            
            for j in range(counting_sort[i]):
                result += i
                if result <= coins:
                    count += 1
                else:
                    break
        
        return count