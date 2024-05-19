# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0
    result = float('inf')
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def findLeft(root, depth):
            if not root:
                return 
            
            left = findLeft(root.left, depth + 1)
            right = findLeft(root.right, depth + 1)

            if root and depth > self.max_depth and not(root.left or root.right):
                self.max_depth = depth
                self.result = root.val
            
            return root

        findLeft(root, self.max_depth)

        return self.result if self.max_depth > 0 else root.val