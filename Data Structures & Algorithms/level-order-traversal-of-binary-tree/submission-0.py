# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes_queue = deque([root])
        result = []

        while nodes_queue:
            level_size = len(nodes_queue)
            nested_nodes = []

            for _ in range(level_size):
                popped_node = nodes_queue.popleft()
                nested_nodes.append(popped_node.val)

                if popped_node.left:
                    nodes_queue.append(popped_node.left)
                if popped_node.right:
                    nodes_queue.append(popped_node.right)
            
            result.append(nested_nodes)
        
        return result