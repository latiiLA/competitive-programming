class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par = [i for i in range(len(isConnected))]
        rank = [1] * (len(isConnected))

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1

            par[p2] = p1

        # Build union and find from the matrix where the cities are connected
        result = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected) - 1):
                if isConnected[i][j] == 1:
                    union(i, j)

        # Loop through the graph and again check the find because we are not using recursion some nodess parent might be the correct parent
        result = set()
        for cell in range(len(isConnected)):
            result.add(find(cell))

        return len(result)


            