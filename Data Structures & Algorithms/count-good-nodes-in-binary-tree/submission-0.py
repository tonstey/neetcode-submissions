# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        stack = []

        def traverse(maximum: int, node: Optional[TreeNode]):
            if not node:
                return 


            if node.val >= maximum:
                nonlocal ans
                ans += 1

            traverse(maximum if maximum >= node.val else node.val, node.left)
            traverse(maximum if maximum >= node.val else node.val, node.right)

        if root:
            traverse(-10000, root)

        return ans
        