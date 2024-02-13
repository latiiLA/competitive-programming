class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cannot_pick = {}
        minimum_card = float('inf')

        # identifies card we cannot pick
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cannot_pick[fronts[i]] = cannot_pick.get(fronts[i], 0) + 1

        # search the minimum card that is not in cannot pick hash map
        for num in (fronts + backs):
            if num not in cannot_pick:
                minimum_card = min(minimum_card, num)

        return minimum_card if minimum_card != float('inf') else 0