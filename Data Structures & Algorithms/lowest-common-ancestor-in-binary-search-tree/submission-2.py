# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def nodeHistory(root: Optional(TreeNode), target: TreeNode, historyArray: List) -> List:
            historyArray.append(root)

            if root.val > target.val:
                nodeHistory(root.left, target, historyArray)
            elif root.val < target.val:
                nodeHistory(root.right, target, historyArray)
            return historyArray

        history_p = nodeHistory(root, p, [])
        history_q = nodeHistory(root, q, [])
    
        history_p = set(history_p)
        for node_value_index in range(len(history_q) - 1, -1, -1):
            print(node_value_index)
            if history_q[node_value_index] in history_p:
                return history_q[node_value_index]
        
        