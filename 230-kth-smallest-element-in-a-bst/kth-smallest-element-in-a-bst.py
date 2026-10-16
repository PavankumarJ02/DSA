# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        num_traversed = 0
        res = None

        def inorder(node):
            nonlocal num_traversed
            nonlocal res

            if num_traversed == k:
                return

            if node.left:
                inorder(node.left)
            
            if num_traversed < k:
                num_traversed += 1
                if num_traversed == k:
                    res = node.val
            else:
                return
            
            if node.right:
                inorder(node.right)

        inorder(root)

        return res