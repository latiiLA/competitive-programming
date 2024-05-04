class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        total = 0
        queue = deque()
        result = float('inf')

        # Calculate the prefix of the array first
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        # add the values to the queue while tracking its sum
        for i, num in enumerate(prefix):
            # create monotonically increasing
            while queue and queue[-1][0] >= num:
                queue.pop()
            
            #  compare the new subarray length with the previous one
            while queue and num - queue[0][0] >= k:
                result = min(i - queue[0][1], result)
                queue.popleft()
            
            queue.append((num, i))
        
        return result if result != float('inf') else -1