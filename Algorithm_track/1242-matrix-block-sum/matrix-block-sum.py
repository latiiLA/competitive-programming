class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # rows, cols = len(mat), len(mat[0])
        # sumMat = [[0] * (cols + 1) for r in range(rows + 1)]

        # for r in range(rows):
        #     prefix = 0
        #     for c in range(cols):
        #         prefix += mat[r][c]
        #         above = sumMat[r][c + 1]
        #         sumMat[r + 1][c + 1] = (prefix + above)

        # print(sumMat)

        # answer = [[0] * cols for _ in range(rows)]

        # for i in range(1, rows):
        #     for j in range(1, cols):
        #         answer[i][j] += prefix[i][j]


        m, n = len(mat), len(mat[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = sum(sum(mat[x][max(0, j-k):min(n, j+k+1)])
                                    for x in range(max(0, i-k), min(m, i+k+1)))
        return result