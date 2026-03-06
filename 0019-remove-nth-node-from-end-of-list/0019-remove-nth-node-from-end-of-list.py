# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # arr = []
        count = 0
        curr = head
        while curr:
            # arr.append(curr.val)
            count += 1
            curr = curr.next

        # x = len(arr) - n
        x = count - n
        # val = arr[x]

        demmy = ListNode(0)
        demmy.next = head

        cur = demmy
        i  = 0
        while cur.next :
            # if cur.next.val == val and i == x:
            if i == x:
                cur.next = cur.next.next
            else:
                cur = cur.next
            i += 1
        return demmy.next