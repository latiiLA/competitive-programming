class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sortedNums = sorted(nums)
        countOfSmallerNumbers = []

        # Loop and find the number elements smaller than the elements for each elements
        for i in range(len(nums)):
            countOfSmallerNumbers.append(sortedNums.index(nums[i]))

        return countOfSmallerNumbers
