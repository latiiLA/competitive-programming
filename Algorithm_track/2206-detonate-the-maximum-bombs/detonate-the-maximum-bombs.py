class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjecency_list = defaultdict(list)
        n = len(bombs)

        # build adjecency list based on their distance from one another and their radius
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                radius = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                if radius <= r1:
                    adjecency_list[i].append(j)
                if radius <= r2:
                    adjecency_list[j].append(i)


        visited = set()
        # build dfs function
        def dfs(bomb):
            if bomb in visited:
                return 0
            visited.add(bomb)
            for neighbour in adjecency_list[bomb]:
                dfs(neighbour)

        result = 0
        # initialize your dfs function for every node
        for i in range(n):
            dfs(i)
            result = max(result, len(visited))
            visited = set() #initialize new set for ever dfs call

        return result

                
