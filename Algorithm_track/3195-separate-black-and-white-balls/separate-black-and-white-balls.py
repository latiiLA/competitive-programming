class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        result = 0

        for char in s:
            if char == '1':
                count += 1
            else:
                result += count

        return result

        