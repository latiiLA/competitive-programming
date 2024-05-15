# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preOrder(root, ans):
            if root == None:
                return
            else:
                ans.append(root.val)
                preOrder(root.left, ans)
                preOrder(root.right, ans)
        
        preOrder(root, ans)
        return ans