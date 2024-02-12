class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count_appearance = {}
        majority = []
        
        # Updates the counts in the dictionary
        for num in nums:
            count_appearance[num] = count_appearance.get(num, 0) + 1

        for key in count_appearance:
            if count_appearance[key] > len(nums)//3:
                majority.append(key)

        return majority
