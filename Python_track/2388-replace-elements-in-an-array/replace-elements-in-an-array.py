class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        index_of_elements = {}
        
        # Finds the index of numbers and stores them in the dictionary as number, index
        for i in range(len(nums)):
            index_of_elements[nums[i]] = i
        
        # performs the operations on the nums using the dictionary index
        for op in operations:
            nums[index_of_elements[op[0]]] = op[1]
            index_of_elements[op[1]] = index_of_elements[op[0]]
        
        return nums