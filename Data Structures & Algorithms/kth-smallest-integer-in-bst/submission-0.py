# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        crt = root
        while crt or st:
            while crt:
                st.append(crt)
                crt = crt.left
            crt = st.pop()
            k = k-1
            if k == 0:
                return crt.val
            crt = crt.right
        return root.val