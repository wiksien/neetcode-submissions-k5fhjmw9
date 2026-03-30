# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        que = deque([root])
        level = 0

        while len(que) != 0:
            level += 1
            
            for number_of_pops in range(0, len(que)):
                working_node = que.popleft()

                if working_node.left != None:
                    que.append(working_node.left)
                if working_node.right != None:
                    que.append(working_node.right)
        
        return level



