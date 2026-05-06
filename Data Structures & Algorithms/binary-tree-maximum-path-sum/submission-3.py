# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(n):
            if n == None:
                return 0

            left, right = max(0, dfs(n.left)), max(0, dfs(n.right))
            
            nonlocal res
            res = max(res, left + right + n.val)
            
            return max(left, right) + n.val
        
        dfs(root)
        return res