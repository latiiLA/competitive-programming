class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        sumMat = [[0] * (cols + 1) for r in range(rows + 1)]

        # Calculate prefix sum for the matrix
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += mat[r][c]
                above = sumMat[r][c + 1]
                sumMat[r + 1][c + 1] = (prefix + above)

        answer = [[0] * cols for _ in range(rows)]

        # Calculate the start end rows and columns. use precalculated result and update your answer
        for i in range(rows):
            for j in range(cols):
                r1 = max(i - k, 0) + 1
                c1 = max(j - k, 0) + 1
                r2 = min(i + k, rows - 1) + 1
                c2 = min(j + k, cols - 1) + 1

                answer[i][j] = sumMat[r2][c2] - sumMat[r1 - 1][c2] - sumMat[r2][c1 - 1] + sumMat[r1 - 1][c1 - 1]

        return answer

        # Another approach gained from leetcode solutions
        
        # m, n = len(mat), len(mat[0])
        # result = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         result[i][j] = sum(sum(mat[x][max(0, j-k):min(n, j+k+1)])
        #                             for x in range(max(0, i-k), min(m, i+k+1)))
        # return result