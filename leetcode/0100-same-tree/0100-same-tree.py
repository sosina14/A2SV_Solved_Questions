# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
   
        def same(node1,node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (node2 and not node1):
                return False
            
            stack1.append(node1)
            stack2.append(node2)

            while len(stack1) > 0 and len(stack2)>0:
                cur1 = stack1.pop()
                cur2 = stack2.pop()

                if cur1.val != cur2.val:
                    return False

                if (cur1.left and not cur2.left) or (not cur1.left and cur2.left):
                        return False

                if (cur1.right and not cur2.right) or (not cur1.right and cur2.right):
                        return False

                if cur1.left:
                    stack1.append(cur1.left)
                if cur2.left:
                    stack2.append(cur2.left)
                if cur1.right:
                    stack1.append(cur1.right)
                if cur2.right:
                    stack2.append(cur2.right)

            return True
        return same(p,q)

