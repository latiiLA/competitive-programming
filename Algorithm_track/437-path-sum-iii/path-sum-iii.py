# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # count the result for each node
        def path(node, sum_):
            if not node:
                return 0

            sum_ += node.val

            count = sum_ == targetSum
            count += path(node.left, sum_)
            count += path(node.right, sum_)

            return count

        # call the function for each node and accumulate the results
        def helper(node):
            if not node:
                return 0
            path_sum = path(node, 0)
            path_sum += helper(node.left)
            path_sum += helper(node.right)

            return path_sum

        return helper(root)


