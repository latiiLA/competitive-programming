class Solution:
    def minSwaps(self, s: str) -> int:
        stack1 = []

        for char in s:
            if char == "[":
                stack1.append(char)
            elif stack1 and char == "]":
                stack1.pop()
            else:
                stack1.append(char)
        return len(stack1) // 2
