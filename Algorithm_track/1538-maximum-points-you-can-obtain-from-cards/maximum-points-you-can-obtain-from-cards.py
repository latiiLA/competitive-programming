class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        result = total

        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            result = max(result, total)
            l += 1
            r += 1

        return result