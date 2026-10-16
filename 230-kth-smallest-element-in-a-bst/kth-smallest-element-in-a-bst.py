class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        return nums[k - 1]
        