# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head
        count = 0

        if not head:
            return head

        while current:
            count+=1
            current = current.next

        if count == 1:
            head= None
            return head

        if count == n:
            return head.next

        r = count-n-1
        current = head

        while r > 0:
            r-=1
            current = current.next

        current.next = current.next.next

        return head

        


        

        
        