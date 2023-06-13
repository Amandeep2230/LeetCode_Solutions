# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        #check if node exists in head
        if not head or not head.next:
            return head
        
        #initialize pointers to dummy
        prev = dummy
        curr = head

        #swap the pairs
        while (curr and curr.next):
            first = curr
            second = curr.next

            prev.next = second
            first.next = second.next
            second.next = first

            #change first and second to correct positions
            prev = first
            curr = first.next

        return dummy.next           