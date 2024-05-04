class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_queue = deque()
        max_queue = deque()
        result = 0
        i = 0

        # track max and minimum value using sliding window. remove the first inserted element using queue.
        for j, num in enumerate(nums):
            # monotonically decreasing queue
            while min_queue and min_queue[-1][1] >= num:
                min_queue.pop()
            min_queue.append((j, num))
            
            # monotonically increasing queue
            while max_queue and max_queue[-1][1] <= num:
                max_queue.pop()
            max_queue.append((j, num))

            # pop if the queue difference are greater than 2
            while max_queue[0][1] - min_queue[0][1] > 2:
                if max_queue[0][0] == i:
                    max_queue.popleft()
                if min_queue[0][0] == i:
                    min_queue.popleft()
                i += 1
            
            result += j - i + 1 # calculate the numer of sub array using the sliding window

        return result


