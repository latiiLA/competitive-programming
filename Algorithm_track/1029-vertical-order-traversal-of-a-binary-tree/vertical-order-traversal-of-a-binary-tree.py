# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary = defaultdict(list) # dictionary to capture the values of every vertical

        def vertical(root, order, level): # recursive function
            if not root:
                return
            dictionary[order].append((level, root.val))
            vertical(root.left, order - 1, level + 1)
            vertical(root.right, order + 1, level + 1)

        vertical(root, 0, 0) # recursive initial call
        
        # sort the keys of the dictionary and then access dictionary according the sorted keys 
        # and sort the value of that key and add to your answer
        sorted_keys = list(dictionary)
        sorted_keys.sort()
        result = []

        for key in sorted_keys:
            dictionary[key].sort() # sort by level
            result.append([node[1] for node in dictionary[key]])

        return result