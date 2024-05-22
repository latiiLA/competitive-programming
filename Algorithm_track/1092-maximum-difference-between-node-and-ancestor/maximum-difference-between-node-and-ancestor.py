# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDifference = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # pass maximum and minimum value and compute the difference on the go and update the global variable
        def findMaxDiff(root, maximum, minimum):
            if not root:
                return 
            
            else:
                maximum = max(root.val, maximum)
                minimum = min(root.val, minimum)
                self.maxDifference = max(self.maxDifference, maximum - minimum)

                findMaxDiff(root.left, maximum, minimum)
                findMaxDiff(root.right, maximum, minimum)
        
        findMaxDiff(root, root.val, root.val)
        return self.maxDifference