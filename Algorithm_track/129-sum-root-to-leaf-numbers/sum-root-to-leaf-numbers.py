# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumation = 0

        # dfs definition
        def dfs(root, total):
            if not root:
                return 0

            total = total * 10 + root.val # calaculate the new total from the previous one

            # update the total sum if it is leaf node
            if not root.left and not root.right:
                self.sumation += total
                return 

            # recursive call
            dfs(root.left, total)
            dfs(root.right, total)

        dfs(root, 0)

        return self.sumation
