# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isValidSubtree(root, subRoot):
            if (not root and subRoot) or (root and not subRoot):
                return False
            
            if not root and not subRoot:
                return True
            
            if root.val == subRoot.val:
                return isValidSubtree(root.left, subRoot.left) and isValidSubtree(root.right, subRoot.right)
            else:
                return False
        
        def dfsTriggerIsValidSubtree(root):
            if not root:
                return False

            if isValidSubtree(root, subRoot):
                return True
            else:
                return dfsTriggerIsValidSubtree(root.left) or dfsTriggerIsValidSubtree(root.right)
        
        return dfsTriggerIsValidSubtree(root)
