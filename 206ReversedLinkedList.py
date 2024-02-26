#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []

        while head:
            l.append(head.val)
            head = head.next

        l.reverse()

        h = ListNode()
        temp = h
        for item in l:
            temp.next = ListNode(item)
            temp = temp.next

        return h.next