# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mid = []
        curr = head

        while (curr):
            mid.append(curr.val)
            curr = curr.next
        
        mid.sort()

        dummy = ListNode(0)
        dummy.next = head

        c = dummy.next
        
        for i in mid:
            c.val = i
            c = c.next
        
        return dummy.next