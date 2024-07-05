class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Multi source bfs --- register all you sources to the queue
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    queue.append([row, col])

        result = -1
        # bfs implementation
        while queue:
            row, col = queue.popleft()

            result = grid[row][col]
            for dx, dy in [[0, 1], [1, 0], [-1,  0], [0, -1]]:
                new_dx = dx + row
                new_dy = dy + col
                # check the boundary
                if (min(new_dx, new_dy) >= 0 and max(new_dx, new_dy) < n and grid[new_dx][new_dy] == 0):
                    queue.append([new_dx, new_dy])
                    grid[new_dx][new_dy] = grid[row][col] + 1

        return -1 if result <= 1 else result - 1