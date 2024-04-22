class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # append and pop based on the criteria
        for char in s:
            if char == '(' or char == "{" or char == "[" or len(stack) == 0:
                stack.append(char)
            elif char == ')' and stack[-1] == '(' or char == ']' and stack[-1] == '[' or char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
                        
        if len(stack) == 0:
            return True
        else:
            return False