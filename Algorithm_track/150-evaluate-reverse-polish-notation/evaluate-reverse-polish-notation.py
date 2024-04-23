class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2 + temp1)
            elif token == "-":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2 - temp1)
            elif token == "*":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2 * temp1)
            elif token == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2 / temp1))
            else:
                stack.append(int(token))

        return stack[-1]