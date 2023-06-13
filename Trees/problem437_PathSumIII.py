# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def calc(node, total):
            if not node:
                return None
            
            total += node.val

            if total == targetSum:
                self.count += 1
            
            calc(node.left, total)
            calc(node.right, total)
        
        def dfs(node):
            if not node:
                return None
            
            calc(node, 0)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.count