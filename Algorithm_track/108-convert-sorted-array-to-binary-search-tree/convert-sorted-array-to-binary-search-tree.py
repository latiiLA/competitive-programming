# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def BST(i, j):
            if i > j:
                return None

            mid = (i + j) // 2
            
            root = TreeNode(nums[mid])
            root.left = BST(i, mid - 1)
            root.right = BST(mid + 1, j)
            return root

        return BST(0, len(nums) - 1)