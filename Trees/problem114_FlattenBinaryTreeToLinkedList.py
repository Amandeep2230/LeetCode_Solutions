# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #flaten root and return tail
        def rearr(root):
            if not root:
                return None
            
            leftTail = rearr(root.left)
            rightTail = rearr(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            last = rightTail or leftTail or root
            return last
        
        rearr(root)