class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for char in s:
            if char != '#':
                stack1.append(char)
            elif char == '#' and len(stack1) > 0:
                stack1.pop()
        
        for char in t:
            if char != '#':
                stack2.append(char)
            elif char == '#' and len(stack2) > 0:
                stack2.pop()

        return stack1 == stack2