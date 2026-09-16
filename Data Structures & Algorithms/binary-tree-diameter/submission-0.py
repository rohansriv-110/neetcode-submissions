# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(node):
            nonlocal res 
            if not node:
                return 0
            L=height(node.left)
            R=height(node.right)
            res=max(res, L+R)
            return 1+max(L,R)

        height(root)
        return res


        
        
        