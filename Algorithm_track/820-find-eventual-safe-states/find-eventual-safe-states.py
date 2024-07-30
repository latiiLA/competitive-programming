class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0 - white     1 - grey      2 - black
        colors = [0 for _ in range(len(graph))]

        def dfs(graph, node, colors):
            # check if there is a cycle
            if colors[node] == 1:
                return False

            colors[node] = 1
            for child in graph[node]:
                if colors[child] == 2:
                    continue
                if not dfs(graph, child, colors):
                    return False

            # update color of node
            colors[node] = 2
            return True


        # do dfs from each node
        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            dfs(graph, i, colors)
        print(colors)
        
        # filter the safe nodes
        answer = []
        for i in range(len(colors)):
            if colors[i] == 2:
                answer.append(i)

        return answer
