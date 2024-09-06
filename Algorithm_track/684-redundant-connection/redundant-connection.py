class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        # find the parent of nodes
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # compression
                p = parent[p]

            return p
        
        # define union function
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)
            # if they have the same parent that means they form cycle, so return False
            if parent1 == parent2:
                return False

            # make the highest rank the parent
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                parent[parent1] = parent2
                rank[parent2] += 1

            return True
        
        # check each and every nodes if they make cycle. if they do return that
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]