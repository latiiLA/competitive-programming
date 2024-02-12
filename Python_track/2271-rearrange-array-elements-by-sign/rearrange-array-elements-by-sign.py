class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        negative_array = []
        positive_array = []

        rearranged_array = []

        # separates negative and positive numbers
        for num in nums:
            if num < 0:
                negative_array.append(num)
            elif num > 0:
                positive_array.append(num)

        for i in range(len(negative_array)):
            rearranged_array.append(positive_array[i])
            rearranged_array.append(negative_array[i])
    
        return rearranged_array
