# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next

        if not array:
            return None
            
        array.reverse()

        head = ListNode(array[0])
        cur = head
        for i in range(1,len(array)):
            cur.next = ListNode(array[i])
            cur = cur.next

        return head
