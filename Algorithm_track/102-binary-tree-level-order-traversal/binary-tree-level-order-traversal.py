# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary = defaultdict(list)

        def levels(root, level):
            if not root:
                return 
            
            dictionary[level].append(root.val)
            levels(root.left, level + 1)
            levels(root.right, level + 1)

        levels(root, 0)

        return [dictionary[key] for key in dictionary.keys()]
