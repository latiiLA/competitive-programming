class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoization = {}
        length = len(coins)
        def dp(i, amount):
            if i >= length or amount < 0:
                return float('inf')
            if amount == 0:
                return 0

            # return from memo if it is already computed
            if (i, amount) in memoization:
                return memoization[(i, amount)]

            # compute the 
            memoization[(i, amount)] = min(dp(i, amount - coins[i]) + 1, dp(i + 1, amount))

            return memoization[(i, amount)]

        ans = dp(0, amount)
        return -1 if ans == float('inf') else ans

            



            