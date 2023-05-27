"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        buffer = { None : None }

        #copy the nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            buffer[curr] = copy
            curr = curr.next
        
        #linking the nodes
        curr = head
        while curr:
            copy = buffer[curr]
            copy.next = buffer[curr.next]
            copy.random = buffer[curr.random]
            curr = curr.next
        
        return buffer[head]