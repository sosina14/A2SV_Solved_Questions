# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # count = 0
        # curr = head
        # while curr :
        #     count += 1
        #     curr = curr.next

        # x = count //2

        # demmy = ListNode(0)
        # demmy.next = head

        # i = 0
        # new = demmy
        # while i < x:
        #     new = new.next
        #     i += 1

        # return new.next
