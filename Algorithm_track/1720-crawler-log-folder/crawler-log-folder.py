class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        result = 0

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue           
            else:
                stack.append(log)

        return len(stack)