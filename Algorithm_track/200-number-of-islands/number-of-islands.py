class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        no_island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        # dfs definition
        def dfs(i, j):
            if grid[i][j] == 0: # if the cell happens to be 0 that is not part of island
                return
        
            visited.add((i, j)) # add the cell to your visited list

            # call the dfs on the neighbouring cells to get all island parts if it is not visited before. also check the boundary 
            for row, col in directions:
                if row + i in range(rows) and col + j in range(cols) and \
                    grid[row + i][col + j] == "1" and (row + i, col + j) not in visited:
                    dfs(row + i, col + j)

        # Find where there is land and call dfs on it, increment your island as well
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1" and (i, j) not in visited:
                    dfs(i, j)
                    no_island += 1

        return no_island