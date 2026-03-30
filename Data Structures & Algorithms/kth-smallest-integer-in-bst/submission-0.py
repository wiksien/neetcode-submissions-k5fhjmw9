# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getValues(root: Optional[TreeNode], result: List) -> List:
            if not root:
                return result
            
            result.append(root.val)
            getValues(root.left, result)
            getValues(root.right, result)

            return result
        
        values_array = sorted(getValues(root, []))

        return values_array[k - 1]
        