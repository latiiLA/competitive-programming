class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjecency = defaultdict(list)

        for u, v in edges:
            adjecency[u].append(v)
            adjecency[v].append(u)

        seen = set()

        # dfs definition
        def dfs(node):
            # base case
            if node == destination:
                return True
            
            seen.add(node) # visited node tracker

            
            for v in adjecency[node]:
                if v not in seen and dfs(v):
                    return True
            
            return False

        return dfs(source)
