class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s, 2)
        result = 0

        while number > 1:
            if number % 2 == 1:
                result += 1
                number += 1
            number //= 2
            result += 1

        return result
