class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else self.isPowerOfFour(n // 4) if n % 4 == 0 else n == 1 