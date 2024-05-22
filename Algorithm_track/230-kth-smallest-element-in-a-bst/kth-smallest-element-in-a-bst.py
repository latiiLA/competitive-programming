# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = [] # build inOrder traversal of the tree and return the kth element
        def smallest(root):
            if not root:
                return
            
            else:
                smallest(root.left)
                inOrder.append(root.val)
                smallest(root.right)

        smallest(root)
        return inOrder[k-1]