# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        q=deque([root])
        d={}
        while q: #Doing this BFS traversal to store the parent nodes in the dictionary
            node=q.popleft()
            if node.left:
                q.append(node.left)
                d[node.left]=node
            if node.right:
                q.append(node.right)
                d[node.right]=node
        q.append(target)
        distance=0
        visited=set() #Do avoid repetition
        visited.add(target)
        while q: # Doing this BFS traversal to get the node at distance k
            for i in range(len(q)):
                node=q.popleft()
                if node in d and d[node] not in visited:
                    q.append(d[node])
                    visited.add(d[node])
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
            distance+=1
            if distance==k:
                break
        ans=[]
        while q: # Storing all the value of all the nodes at distance k in array
            node=q.popleft()
            ans.append(node.val)
        return ans