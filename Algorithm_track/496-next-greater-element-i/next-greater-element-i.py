class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        result = [-1] * n
        stack = [nums2[0]]
        dictionary = {}

        # loop through the num2 and find the largest element
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                dictionary[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        # check the dictionary for the result        
        for i, num in enumerate(nums1):
            if num in dictionary:
                result[i] = dictionary[num]

        return result    

