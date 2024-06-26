# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.total = 0

        def path(node, tot):
            if not node:
                return 0

            tot += node.val
            if tot == targetSum:
                self.total += 1
            path(node.left, tot)
            path(node.right, tot)

        def bfs(node):
            queue = deque([node])
            while queue:
                current = queue.pop()
                path(current, 0)
                if current:
                    queue.append(current.left)
                    queue.append(current.right)

        bfs(root)

        return self.total
        
