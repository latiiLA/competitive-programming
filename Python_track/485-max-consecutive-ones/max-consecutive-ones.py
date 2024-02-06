class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        counter = 0

        for num in nums:
            if num == 1:
                
                count += 1
                print(count)
            elif num == 0:
                counter = max(counter, count)
                count = 0
        
        return max(counter, count)