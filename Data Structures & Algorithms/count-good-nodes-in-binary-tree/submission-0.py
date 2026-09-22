# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):                       # visit node, knowing the path max
            if not node:                             # empty spot
                return 0                             # no good nodes here
            res = 1 if node.val >= maxVal else 0     # is this node good?
            maxVal = max(maxVal, node.val)           # update the path max
            res += dfs(node.left, maxVal)            # add good nodes on the left
            res += dfs(node.right, maxVal)           # add good nodes on the right
            return res                               # total for this subtree

        return dfs(root, root.val)                   # start at the root; root is always good



        