# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        if leftheight-rightheight<=1 and leftheight-rightheight>=-1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)  
        else:
            return False