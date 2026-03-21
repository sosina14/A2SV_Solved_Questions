# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        stack = [root]

        while stack:
            cur = stack.pop()

            if cur.val == subRoot.val:
                newstack = [(cur, subRoot)]
                flag = True

                while newstack:
                    n1, n2 = newstack.pop()

                    if n1.val != n2.val:
                        flag = False
                        break

                    if (n1.left is None) != (n2.left is None):
                        flag = False
                        break

                    if (n1.right is None) != (n2.right is None):
                        flag = False
                        break

                    if n1.left:
                        newstack.append((n1.left, n2.left))
                    if n1.right:
                        newstack.append((n1.right, n2.right))

                if flag:
                    return True


            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return False
