class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for red in redEdges:
            graph[red[0]].append((red[1], 0))
        
        for blue in blueEdges:
            graph[blue[0]].append((blue[1], 1))

        # declare variables
        result = [-1] * n
        queue = deque([(0, 0, None)])
        visited = set()

        # implement dfs
        while queue:
            node, dist, prev_edge = queue.popleft()
            visited.add((node, prev_edge))
            
            if result[node] == -1:
                result[node] = dist
            for neighbour, edge in graph[node]:
                if (neighbour, edge) not in visited and prev_edge != edge:
                    queue.append((neighbour, dist+1, edge))
        
        return result