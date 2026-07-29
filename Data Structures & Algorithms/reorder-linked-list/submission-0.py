# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        h = head.next
        t = head

        while h and h.next:
            h = h.next.next
            t = t.next
            

        
        prev = None
        current = t.next
        t.next = None
        while current:
            new_node = current.next
            current.next = prev
            prev = current 
            current = new_node


        first,second  =head, prev


        while second:
            temp_1 = first.next
            temp_2 = second.next

            first.next = second
            second.next = temp_1

            first = temp_1
            second = temp_2

            
        