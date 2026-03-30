# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        F = S = head

        while F != None:
            if F.next == None:
                return False
            F = F.next.next
            S = S.next
            if F == S:
                return True
        
        return False
        

        