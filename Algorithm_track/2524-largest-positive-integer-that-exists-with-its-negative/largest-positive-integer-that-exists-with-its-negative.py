class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dictionary = {}
        result = -1

        # check if the opposite negative or positive value exits else return store the opposite value current number
        for num in nums:
            if num in dictionary:
                result = max(result, abs(num))
            else:
                dictionary[num * -1] = 1
        
        return result

