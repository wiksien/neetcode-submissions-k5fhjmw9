# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getValuesDesc(root: Optional[TreeNode], result: List) -> List:
            if not root:
                return result
            
            if root.right:
                getValuesDesc(root.right, result)
            
            result.append(root.val)
            getValuesDesc(root.left, result)

            return result
        
        current = root
        sorted_values = getValuesDesc(root, [])

        return sorted_values[-k]
        