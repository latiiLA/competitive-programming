class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]

        for rich_x, rich_y in richer:
            graph[rich_x].append(rich_y)
            indegree[rich_y] += 1
        
        # print(graph, indegree)

        # start bfs
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # bfs implementation
        answer = [_ for _ in range(n)] # initialize your answer
        while queue:
            current = queue.popleft()

            for child in graph[current]:
                # compare the answer of the parents with the current parent quetness
                if quiet[answer[child]] > quiet[answer[current]]:
                    answer[child] = answer[current]
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return answer