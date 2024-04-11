class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        prefix = [1] * (n + 1)
        suffix = 1
        answer = [[1] * cols for _ in range(rows)]

        # Use Modulo appropr

        # Calculate suffix on the answer matrix it self
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                answer[i][j] *= suffix
                answer[i][j] %= 12345
                suffix *= grid[i][j] % 12345

        # Calculate prefix on the asnwer array itself while moduling the array with specified number
        current = 1
        for i in range(rows):
            for j in range(cols):
                answer[i][j] *= current
                answer[i][j] %= 12345
                current = (current * grid[i][j]) % 12345

        return answer