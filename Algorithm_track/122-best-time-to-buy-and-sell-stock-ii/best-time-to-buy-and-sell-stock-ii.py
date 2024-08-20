class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memoization = {}

        def dp(i, holding):
            if i >= n:
                return 0  # Base case: No more days, no more profit

            if (i, holding) in memoization:
                return memoization[(i, holding)]

            do_nothing = dp(i + 1, holding)
            if holding:
                do_something = dp(i + 1, False) + prices[i] # sell
            else:
                do_something = dp(i + 1, True) - prices[i] # buy

            memoization[(i, holding)] = max(do_nothing, do_something)
            return memoization[(i, holding)]

        # Start with not holding any stock
        return dp(0, False)
