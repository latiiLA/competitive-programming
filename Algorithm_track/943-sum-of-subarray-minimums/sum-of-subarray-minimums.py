class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10 ** 9 + 7
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        result = 0

        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                index, m = stack.pop()
                right = index - stack[-1][0] if stack else index + 1
                left = i - index
                result = (result + m * right * left) % MOD
            
            stack.append((i, num))
        
        return result