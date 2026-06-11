# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self,root:Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.right==None and root.left==None:
            return 0
        while root:
            if root.left==None and root.right:
                root=root.right
                self.diameterOfBinaryTree(root)
            elif root.right==None and root.left:
                root=root.left
                self.diameterOfBinaryTree(root)
            elif root.left and root.right:
                return self.maxDepth(root.right)+self.maxDepth(root.left)
            elif root.left==None and root.right==None:
                return self.maxDepth(root)

            