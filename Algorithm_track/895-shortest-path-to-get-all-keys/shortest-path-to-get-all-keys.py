from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        # Check if a position is valid
        isValid = lambda x, y: 0 <= x < n and 0 <= y < m

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col, 0, frozenset())])
            visited = set()
            visited.add((start_row, start_col, frozenset()))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue:
                row, col, move, collected_keys = queue.popleft()

                # Base case: all keys have been collected
                if len(collected_keys) == len(allKeys):
                    return move
            
                if grid[row][col] == '#': # wall
                    continue
                
                if grid[row][col].islower():
                    new_keys = collected_keys | frozenset([grid[row][col]])
                else:
                    new_keys = collected_keys

                # If it's a lock, ensure we have the corresponding key
                if grid[row][col].isupper() and grid[row][col].lower() not in collected_keys:
                    continue

                # Branch into for possible directions directions
                for dx, dy in directions:
                    new_r, new_c = row + dx, col + dy
                    if isValid(new_r, new_c) and (new_r, new_c, new_keys) not in visited:
                        queue.append((new_r, new_c, move + 1, new_keys))
                        visited.add((new_r, new_c, new_keys))

            return -1  # if it is impossible

        start_row = start_col = -1
        allKeys = set()

        # Find start position and all keys
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start_row, start_col = i, j
                if grid[i][j].islower():
                    allKeys.add(grid[i][j])

        ans = bfs(start_row, start_col)

        return -1 if ans == -1 else ans - 1



# class Solution:
#     def shortestPathAllKeys(self, grid: List[str]) -> int:
#         n = len(grid)
#         m = len(grid[0])
        
#         # Check if a position is valid
#         isValid = lambda x, y: 0 <= x < n and 0 <= y < m

#         def bfs(start_row, start_col):
#             queue = deque([(start_row, start_col, 0, "")])  # (row, col, move count, collected keys)
#             visited = set()
#             directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#             while queue:
#                 row, col, move, collected_keys = queue.popleft()

#                 # If we have collected all keys, return the move count
#                 if len(collected_keys) == len(allKeys):
#                     return move
                
#                 # Mark this state as visited
#                 if (row, col, collected_keys) in visited:
#                     continue
#                 visited.add((row, col, collected_keys))

#                 # Check if the current cell is a wall
#                 if grid[row][col] == '#':
#                     continue
                
#                 # Collect the key if it's on the current cell
#                 if grid[row][col].islower():
#                     if grid[row][col] not in collected_keys:
#                         collected_keys += grid[row][col]
#                         collected_keys = ''.join(sorted(collected_keys))  # Keep keys sorted
                
#                 # If it's a lock, ensure we have the corresponding key
#                 if grid[row][col].isupper():
#                     if grid[row][col].lower() not in collected_keys:
#                         continue

#                 # Explore all 4 possible directions
#                 for dx, dy in directions:
#                     new_r, new_c = row + dx, col + dy
#                     if isValid(new_r, new_c):
#                         queue.append((new_r, new_c, move + 1, collected_keys))

#             return -1  # If no solution, return -1

#         start_row = start_col = -1
#         allKeys = set()

#         # Find start position and all keys
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '@':
#                     start_row, start_col = i, j
#                 if grid[i][j].islower():
#                     allKeys.add(grid[i][j])

#         # Perform BFS to find the shortest path to collect all keys
#         ans = bfs(start_row, start_col)

#         return -1 if ans == -1 else ans - 1


# class Solution:
#     def shortestPathAllKeys(self, grid: List[str]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         visited = set()
#         keys = set()
#         isValid = lambda x, y: 0 <= x < n and 0 <= y < m

#         def bfs(r, c, move):
#             queue = deque([(r, c, move)])            
#             directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#             moves = float('inf')

#             while queue:
#                 print(keys)
#                 row, col, move = queue.popleft()
#                 if len(keys) == len(allKeys):
#                     return move

#                 if grid[row][col] == '#':
#                     continue
#                 if grid[row][col].islower():
#                     keys.add(grid[row][col])

#                 if grid[row][col].isupper():
#                     if grid[row][col].lower() not in keys:
#                         continue

#                 for dx, dy in directions:
#                     new_r, new_c = r + dx, c + dy
#                     if isValid(new_r, new_c) and (new_r, new_c) not in visited:
#                         queue.append((new_r, new_c, move + 1))
#                         visited.add((new_r, new_c))

#             return -1

#         start_row = -1
#         start_col = -1
#         allKeys = set()
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '@':
#                     start_row = i
#                     start_col = j

#                 if grid[i][j].islower():
#                     allKeys.add(grid[i][j])
#         print(allKeys, keys)
        
#         minimum_moves = bfs(start_row, start_col, 0)
#         return -1 if minimum_moves == float('inf') else minimum_moves

















#         # visited = set()
#         # keys = set()
#         # totalMoves = 0
#         # directions = [[0,1],[1,0],[-1,0],[0,-1]]

#         # def inbound(row,col):
#         #     return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])

#         # def dfs(row,col,moves):
            
#         #     if not inbound(row,col) or grid[row][col] == '#':
#         #         return
            
#         #     moves += 1
#         #     if grid[row][col].islower():
#         #         keys.add((row,col))
#         #         totalMoves = moves
            
#         #     for dx, dy in directions:
#         #         newRow = row+dx
#         #         newCol = col+dy
#         #         if (newRow,newCol) not in visited:
#         #             dfs(newRow,newCol, moves)
#         #             moves -= 1
        
        
#         # for row in range(len(grid)):
#         #     for col in range(len(grid[0])):
#         #         if grid[row][col] == '@':
#         #             visited.add((row,col))
#         #             dfs(row,col,0)

#         # return totalMoves