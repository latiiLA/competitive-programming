class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        result = 0

        # loop through the string and append and pop characters
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                result += 1

        return result + len(stack)