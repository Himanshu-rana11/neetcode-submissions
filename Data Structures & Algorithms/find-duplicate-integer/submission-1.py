class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize both pointers at the "head" of the linked list (index 0)
        slow = 0
        fast = 0
        
        # Phase 1: Find the intersection point in the cycle
        while True:
            # Move slow pointer 1 step (this is exactly like slow = slow.next)
            slow = nums[slow]
            
            # Move fast pointer 2 steps (this is exactly like fast = fast.next.next)
            fast = nums[nums[fast]]
            
            # Once they meet, we know we are somewhere inside the cycle
            if slow == fast:
                break
                
        # Phase 2: Find the actual entrance to the cycle (the duplicate number)
        slow2 = 0
        while True:
            # Move both pointers 1 step at a time
            slow = nums[slow]
            slow2 = nums[slow2]
            
            # The moment they meet again, that index is the start of the cycle!
            if slow == slow2:
                return slow
        