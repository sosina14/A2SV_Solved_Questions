# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        stack = []
        def sosi(node):
            summ = 0
            if not node: return 0
            stack.append(node)
            while len(stack) > 0:
                cur = stack.pop()
                if cur.val % 2 == 0:
                    if cur.left: 
                        if cur.left.left: summ += cur.left.left.val
                    if cur.left: 
                        if cur.left.right: summ += cur.left.right.val
                    if cur.right: 
                        if cur.right.left: summ += cur.right.left.val
                    if cur.right: 
                        if cur.right.right: summ += cur.right.right.val

                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)

            return summ
        return sosi(root)
