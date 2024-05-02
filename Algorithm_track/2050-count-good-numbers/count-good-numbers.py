class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Take a lesson from finding x power of n using recursion
        # there 5 even numbers for one digit and 4 prime numbers for one digit
        # so for n number of digits you can see the pattern. half of the digits are prime and others are even
        def goodNumbers(x, y):
            if y == 0:
                return 1

            ans = goodNumbers(x, y // 2) % MOD
            ans = (ans * ans) % MOD

            return ans if y % 2 == 0 else ans * x % MOD
        
        result = (((goodNumbers(5, abs(n) // 2 + n % 2)) % MOD) * ((goodNumbers(4, abs(n) // 2)) % MOD) % MOD)

        return 1 / result if n < 0 else result



        # Recursion depth exceeded
        # if n == 0:
        #     return 1

        # return ((4 if n % 2 == 0 else 5) * self.countGoodNumbers(n - 1)) % (10 ** 9 + 7)
        