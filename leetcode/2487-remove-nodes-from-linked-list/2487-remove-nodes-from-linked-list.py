# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        # nxt = stack[0]
        i = 0
        new_node = ListNode()
        cur = stack[0]
        new_node.next = cur
        while i < len(stack)-1:
            cur = stack[i]
            nxt = stack[i+1]
            cur.next = nxt
            i += 1
        
        return new_node.next


        # stack = []
        # cur = head
        
        # while cur:
        #     while stack and stack[-1] < cur.val:
        #         stack.pop()
        
        #     stack.append(cur)
        #     cur = cur.next

     
        # newlist = ListNode()
        # dummy = ListNode()
        # dummy.next = newlist

        # for i in stack:
        #     newnode = ListNode(i)
        #     newlist.next = newnode
        #     newlist = newnode

        # return dummy.next

        