class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else self.isPowerOfThree(n // 3) if n % 3 == 0 else n == 1