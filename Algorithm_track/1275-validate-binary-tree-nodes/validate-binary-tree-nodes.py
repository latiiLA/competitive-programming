class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False

        if root == -1:
            return False

        # Validate the tree using DFS or BFS
        stack = [root]
        visited = defaultdict(bool)
        
        while stack:
            node = stack.pop()
                
            if visited[node]: 
                return False
            
            n -= 1
            visited[node] = True
            
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])
        
        return n == 0