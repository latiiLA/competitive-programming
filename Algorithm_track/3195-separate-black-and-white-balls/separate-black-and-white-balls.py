class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        stack = []

        s = [int(char) for char in s]

        for char in s:
            if char == 1:
                stack.append(1)
            else:
                count += len(stack)

        return count

        