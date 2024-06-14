# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        answer = []

        # inorder traversal
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            answer.append(root.val)
            inorder(root.right) 

        inorder(root)

        def backtracking(i, j):
            if i > j:
                return None

            mid = (i + j)//2 
            root = TreeNode(answer[mid])
            root.left = backtracking(i, mid - 1)
            root.right = backtracking(mid + 1, j)

            return root

        return backtracking(0, len(answer) - 1)   