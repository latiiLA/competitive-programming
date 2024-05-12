class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(grid, a, b):
            maximum = 0
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    maximum = max(maximum, grid[i][j])
            
            return maximum


        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                result[i][j] = find_max(grid, i, j)
        
        return result