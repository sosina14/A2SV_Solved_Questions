# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        if not flag:
            return 

        slow = head
        # count = 0
        while slow != fast:
            slow = slow.next
            fast = fast.next
            # count += 1

        return slow