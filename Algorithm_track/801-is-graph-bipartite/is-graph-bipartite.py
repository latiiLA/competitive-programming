class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        # dfs implementation
        def dfs(i, col):
            if i in color:
                return col == color[i]
            color[i] = col

            # If the color the dfs contradict each other return False else True
            for num in graph[i]:
                if not dfs(num, 1 - col):
                        return False
            return True

        # if the node is not visited before call dfs on it.
        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 1):
                    return False

        return True



            