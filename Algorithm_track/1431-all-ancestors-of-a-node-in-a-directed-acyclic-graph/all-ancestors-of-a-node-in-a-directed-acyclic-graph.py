class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]

        for parent, child in edges:
            graph[parent].append(child)
            indegree[child] += 1
        
        # for zero indegree do bfs
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # bfs implementation to find 
        ancestors = [set() for _ in range(n)]
        while queue:
            current = queue.popleft()
            for child in graph[current]:
                ancestors[child].add(current)
                ancestors[child].update(ancestors[current])

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        # sort
        for i in range(len(ancestors)):
            ancestors[i] = sorted(ancestors[i])

        return ancestors