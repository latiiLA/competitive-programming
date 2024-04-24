class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        # push 0 if the bracket is opening else pop the top value and append the stack with appropriete value
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                temp = stack.pop()
                if temp == 0:
                    stack[-1] += 1
                else:     
                    stack[-1] += temp * 2

        return stack.pop()