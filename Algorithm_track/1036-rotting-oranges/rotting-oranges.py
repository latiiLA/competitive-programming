class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque([])
        visited = set()
        fresh = 0
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # bfs implementation
        while fresh and queue:
            result += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # move to the four directions anc make the good oranges bad
                for dx, dy in directions:
                    new_x = dx + x
                    new_y = dy + y

                    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                        continue
                    if grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2:    
                        continue
                        
                    fresh -= 1 # minimize the number of good oranges

                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))

        return result if fresh == 0 else -1
