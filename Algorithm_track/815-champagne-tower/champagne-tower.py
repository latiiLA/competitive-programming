class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * 101 for _ in range(101)]
        glasses[0][0]=poured

        for i in range(query_row + 1):
            for j in range(i+1):
                excess = (glasses[i][j]-1)/2.0
                if excess > 0:
                    glasses[i+1][j]+=excess
                    glasses[i+1][j+1]+=excess
        return min(1,glasses[query_row][query_glass])
