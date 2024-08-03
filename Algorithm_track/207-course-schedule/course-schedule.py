class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        # build the graph
        for i in range(len(prerequisites)):
            course, pre = prerequisites[i]
            graph[pre].append(course)
            indegree[course] += 1

        # print(graph, indegree)

        # acquire the nodes with zero indegree. that means they are independent/parent
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        # implement bfs
        # process a children of courses while adding them to the result
        # when processing the children decrement the indegree of the childrens hence we processed their parent
        while queue:
            current = queue.popleft()
            result.append(current)

            for course in graph[current]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

        # checks if there is a cycle
        if len(result) != numCourses:
            return []

        return result