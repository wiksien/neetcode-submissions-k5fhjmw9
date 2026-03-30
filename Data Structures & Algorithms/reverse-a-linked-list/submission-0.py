# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], previous_node: Optional[ListNode] = None) -> Optional[ListNode]:
        if not head:
            return previous_node
        
        next_node = head.next
        
        head.next = previous_node
        
        return self.reverseList(next_node, head)
        