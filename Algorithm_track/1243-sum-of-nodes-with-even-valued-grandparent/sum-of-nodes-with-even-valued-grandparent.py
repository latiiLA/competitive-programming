# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0

        def dfs(root, parent=None, gparent=None):
            if not root:
                return

            if gparent and gparent % 2 == 0:
                self.total += root.val
            
            dfs(root.right, root.val, parent)
            dfs(root.left, root.val, parent)

        dfs(root)

        return self.total
