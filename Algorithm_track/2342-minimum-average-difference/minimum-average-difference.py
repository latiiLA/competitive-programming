class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [0]
        total = 0
        n = len(nums)
        minDiff = [float(inf), 0] # track the index and the minimum value
        
        # Calculate the total sum as well as prefix sum
        for num in nums:
            prefix.append(prefix[-1] + num)
            total += num

        # loop though the prefix sum and calculate the left and the right sum, then their average then compute the minimum diff
        for i in range(1, n):
            diff = abs((prefix[i] // i) - ((total - prefix[i]) // (n-i)))
            
            if minDiff[0] > diff:
                minDiff[0] = diff
                minDiff[1] = i - 1

        # calculate incase the total sum can give us the minimum average
        if minDiff[0] > total // n:
            minDiff[0] = total
            minDiff[1] = n - 1

        return minDiff[1]



