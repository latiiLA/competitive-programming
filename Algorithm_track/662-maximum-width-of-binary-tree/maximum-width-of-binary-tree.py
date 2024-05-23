# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dictionary = defaultdict(list)
        dictionary[0].append(1)
        level = 1
        index = 1
        result = 1
        # loop thought the array and calculate the number of elements at that depth using the tree property
        # left element of a node is at 2 * i if i is at its parent
        # right element of a node is at 2 * i + 1 if i is at its parent
        def width(root, index, level):
            if not root:
                return
            
            # update the index and levels
            level += 1
            index = 2 * index
            if root.left:
                dictionary[level].append(index)
            if root.right:
                dictionary[level].append(index + 1)

            # recursive call
            width(root.left, index, level)
            width(root.right, index + 1, level)
        
        width(root, index, level) # call the defined function

        # loop through the stored values in the dictionary and calculate the max and min difference at each level to get the width of the level
        # calculate the maximum width of between the levels and return
        for levels in dictionary:
            min_ = float('inf')
            max_ = float('-inf')
            for level in dictionary[levels]:
                min_ = min(min_, level)
                max_ = max(max_, level)
            result = max(result, max_ - min_ + 1)

        return result

        

            