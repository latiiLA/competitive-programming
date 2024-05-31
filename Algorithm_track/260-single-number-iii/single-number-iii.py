class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dictionary = Counter(nums)
        result = []

        # count the elements and check if the element existed only ance and add it to your result
        for num in dictionary:
            if dictionary[num] == 1:
                result.append(num)

        return result