class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # bfs definition to 
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            
            while queue:
                current = queue.popleft()

                for neighbour in rooms[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

            if len(visited) < len(rooms):
                return False

            return True

        return bfs(0)
            