# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first_node = prev

        if n != 1:
            while (n - 2) > 0:
                prev = prev.next
                n -= 1
        else:
            first_node = first_node.next
        
        if prev.next.next != None:
            prev.next = prev.next.next
        else:
            prev.next = None

        prev, curr = None, first_node

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


        
            
        