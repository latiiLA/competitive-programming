class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memoization = {}

        def dp(i):
            if i >= len(questions):
                return 0

            if i in memoization:
                return memoization[i]

            memoization[i] = max(questions[i][0] + dp(i + 1 + questions[i][1]), dp(i + 1)) # jump the required jump, based on the scenario stated

            return memoization[i]
  
        return dp(0)
            