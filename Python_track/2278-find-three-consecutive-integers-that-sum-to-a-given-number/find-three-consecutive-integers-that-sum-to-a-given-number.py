class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        sum_of_three = []

        if num % 3 != 0:
            return sum_of_three
        
        sum_of_three.append(num//3 - 1)
        sum_of_three.append(num//3)
        sum_of_three.append(num//3 + 1)

        return sum_of_three
