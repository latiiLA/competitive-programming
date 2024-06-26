class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = n * -1
            x = 1 / x
            return x * self.myPow(x, n - 1)
        elif n % 2 == 0:
            y = self.myPow(x, n / 2)
            return y * y
        else:
            return x * self.myPow(x, n - 1)