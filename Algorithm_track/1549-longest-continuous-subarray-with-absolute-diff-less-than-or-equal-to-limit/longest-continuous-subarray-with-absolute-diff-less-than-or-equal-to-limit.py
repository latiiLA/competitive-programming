class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        result = 0

        j = 0 # start of the array
        for i, num in enumerate(nums):
            # create a monotonic array to track a decresing element
            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            min_queue.append(i)

            # create an monotonic array to track increasing element
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            max_queue.append(i)

            # move your second pointer when the limit exceeds
            if nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if nums[max_queue[0]] == nums[j]:
                    max_queue.popleft()
                if nums[min_queue[0]] == nums[j]:
                    min_queue.popleft()
                j += 1
            
            result = max(result, i - j + 1)

        return result