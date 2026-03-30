# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkIfEqual(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return checkIfEqual(root.left, subRoot.left) and checkIfEqual(root.right, subRoot.right)
        
        if not root:
            return False

        if checkIfEqual(root, subRoot) == True:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        