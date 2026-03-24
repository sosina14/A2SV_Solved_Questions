# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            l = float('inf')
            r = float('inf') 

            if node.left:
                l = depth(node.left)
            if node.right:
                r = depth(node.right)
         
            return min(l,r)+1

        return depth(root)