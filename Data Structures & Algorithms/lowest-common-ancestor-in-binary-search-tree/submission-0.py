# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def traverse(node:TreeNode):
            if node.val == p.val or node.val == q.val:
                return node
            elif node.val <=p.val and node.val <= q.val:
                return traverse(node.right)
            elif node.val >= p.val and node.val >= q.val:
                return traverse(node.left)
            else:
                return node

        return traverse(root)