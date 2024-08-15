class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memoization = {}
        length = len(coins)
        def dp(i, amount):
            if i >= length or amount < 0:
                return 0
            if amount == 0:
                return 1

            # return from memo if it is already computed
            if (i, amount) in memoization:
                return memoization[(i, amount)]

            # compute the memoization
            memoization[(i, amount)] = dp(i, amount - coins[i]) + dp(i + 1, amount)

            return memoization[(i, amount)]

        ans = dp(0, amount)
        return 0 if ans == float('inf') else ans

            



            