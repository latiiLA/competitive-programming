class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # compute two different scores. when player 1 choses the max of choosing from the left and right
        def score(left, right):
            if left > right:
                return 0

            score_from_left = nums[left] - score(left + 1, right)
            score_from_right = nums[right] - score(left, right - 1)

            return max(score_from_left, score_from_right)

        return score(0, len(nums) - 1) >= 0