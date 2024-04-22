class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        # if the char is not * push else pop
        for char in s:
            if char is not "*":
                stack.append(char)
            else:
                stack.pop()
        
        return "".join(stack)