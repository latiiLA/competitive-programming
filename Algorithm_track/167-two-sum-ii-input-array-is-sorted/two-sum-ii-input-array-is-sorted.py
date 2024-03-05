class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        # if sumation of the two pointers pointed at the beginning and end is greater than target decrease j otherwise increase i else return result
        while i < j:
            twoSum = numbers[i] + numbers[j]
            if twoSum > target:
                j -= 1
            elif twoSum < target:
                i += 1
            else:
                return [i+1, j+1]
            