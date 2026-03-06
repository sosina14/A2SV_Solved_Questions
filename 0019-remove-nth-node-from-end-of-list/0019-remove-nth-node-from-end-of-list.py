# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        x = len(arr) - n
        val = arr[x]

        demmy = ListNode(0)
        demmy.next = head

        cur = demmy
        i  = 0
        while cur.next :
            if cur.next.val == val and i == x:
                cur.next = cur.next.next
            else:
                cur = cur.next
            i += 1
        return demmy.next