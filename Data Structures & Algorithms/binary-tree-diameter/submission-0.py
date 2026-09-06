# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0 

        def traverse(root):
            nonlocal max_dia
            if root is None:
                return 0
            
            l = traverse(root.left)
            r = traverse(root.right)

            max_dia = max(max_dia,l+r)

            return 1 + max(l,r)
        traverse(root)
        return max_dia
        