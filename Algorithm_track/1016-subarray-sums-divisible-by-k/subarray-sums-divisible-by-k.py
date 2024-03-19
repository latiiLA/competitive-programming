class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # n = len(nums)

        # maximum_sum = sum(nums)
        # max_sum = 0

        # count = 0

        # # Loop through the array and find the minimize the prefix sum when you loop through the elements
        # for i in range(n):
        #     j = n-1

        #     if i > 0:
        #         maximum_sum = maximum_sum - nums[i-1]
            
        #     max_sum = maximum_sum

            
            
        #     while  j >= i:
        #         if max_sum % k == 0:
        #             count += 1
        #         max_sum -= nums[j]
        #         j -= 1

        # return count


        count = 0
        prefix_sum = 0
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1  # We start with 0 so that the prefix sum itself can be divisible by k

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # Increment the count
            count += remainder_counts[remainder]

            # Increment the count of the current remainder.
            remainder_counts[remainder] += 1

        return count


