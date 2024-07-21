class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        double = []

        if maxDoubles == 0:
            return target - 1

        moves = 0

        while target > 1:
            if maxDoubles and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            elif maxDoubles and target % 2 != 0:
                target -= 1
                moves += 1
            else:
                moves += (target - 1)
                target = 1

        return moves