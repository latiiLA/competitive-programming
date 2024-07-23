class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # direction of allowed movements
        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}
        
        queue = deque([(0, 0)]) # queue initialization with the first cell
        grid[0][0] = -grid[0][0] # mark the first cell as visited
        isValid = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) # check the boundary

        while queue:
            i, j = queue.popleft()
            if i == len(grid) - 1 and j == len(grid[0]) - 1: return True # bfs end with when it reaches the bottom right cell

            # apply bfs for all valid neighbours depending on their allowed movement, wether they are visited or not and if they are inside the cells
            for k, l, d in [(i - 1, j, up), (i + 1, j,  down), (i, j - 1, left), (i, j + 1, right)]:
                if isValid(k, l) and -grid[i][j] in d and grid[k][l] in d[-grid[i][j]]:
                    grid[k][l] = -grid[k][l]
                    queue.append((k, l))

        return False