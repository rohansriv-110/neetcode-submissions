# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):                                    # returns [balanced?, height]
            if not node:                                  # empty spot
                return [True, 0]                          # balanced, height 0
            left = dfs(node.left)                         # left child's report
            right = dfs(node.right)                       # right child's report
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])] # my report to parent

        return dfs(root)[0]                               # only the yes/no


         

        

        