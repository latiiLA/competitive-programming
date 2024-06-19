class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visit = set()

        # dfs implementation
        def dfs(i, j):
            # This adds if the neighbour is either water or the the edge it adds to the perimeter
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visit: # if the cell is already visited the perimeter is already calculated
                return 0

            visit.add((i, j)) # add the visited cell to the visit set

            # recursion call for all neighbouring cells
            perimeter = dfs(i, j + 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i - 1, j)

            return perimeter

        # Initially finding the cell where there is a land. from there we can find the neighbouring cells
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j) # call initial dfs function when you find land