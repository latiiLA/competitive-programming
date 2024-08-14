class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands():
            visited = set()
            
            def dfs(r, c):
                stack = [(r, c)]
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        visited.add((i, j))
                        dfs(i, j)
            return islands
        
        if count_islands() != 1:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2
