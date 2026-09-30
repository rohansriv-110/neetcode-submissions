class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        self.pre = 0

        def build(left, right):
            if left > right:
                return None
            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)
            mid = idx[val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)



        
        
 












        
        