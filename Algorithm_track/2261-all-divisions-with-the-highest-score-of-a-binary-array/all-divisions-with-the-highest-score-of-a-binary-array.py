class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # calculate prefix sum
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + int(num == 0))
        prefix.append(0)

        total = sum(nums) # total sum
        dictionary = defaultdict(list)
        maximum = current = 0

        # loop through the prefix and calculate the left and right number of 0 and 1, also find the maximum
        for i in range(1, n + 2):
            temp = prefix[i - 1] + total - current
            maximum = max(maximum, temp)
            dictionary[temp].append(i - 1)
            if i < n + 1:
                current += nums[i - 1]

        return dictionary[maximum]




        # total_sum = sum(nums) # to find the total sum.

        # count_0 = 0
        # count_1 = sum(nums)

        # total_dict = defaultdict(list) # this stores total count of every loop
        # max_count = float('-inf') # this is to find the maximum count
        
        # total_dict[count_1].append(0)

        # # this calculates the left and right sum and updates the dictionary with total count while also finding maximum count
        # for i in range(len(nums)):
        #     count_0 += int(nums[i] == 0)
        #     count_1 -= int(nums[i] == 1)
        #     total = count_0 + count_1
        #     total_dict[total].append(i+1)
        #     max_count = max(max_count, total)

        #     print(total_dict)
    
        # return total_dict[max_count]


        # cnt_1 = 0
        # for num in nums:
        #     if num == 1: cnt_1 += 1
        
        # cnt_0, max_division = 0, cnt_1
        # d = collections.defaultdict(list)
        # d[cnt_1].append(0)
        # for i, num in enumerate(nums):
        #     cnt_0 += int(num == 0)
        #     cnt_1 -= int(num == 1)
        #     d[cnt_0 + cnt_1].append(i + 1)
        #     max_division = max(max_division, cnt_0 + cnt_1)
        # return d[max_division]

                
                