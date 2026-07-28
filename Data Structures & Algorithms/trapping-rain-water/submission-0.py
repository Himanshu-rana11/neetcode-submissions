class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]* n
        right = [0] * n
        total = 0

        for i in range(n):
            if i != 0:
                left[i] = max(height[i-1],left[i-1])

        for i in range(n-1,-1,-1):
            if i+1 != n:
                right[i] = max(height[i+1],right[i+1])

        for i in range(n-1):
            if height[i] < left[i] and height[i] < right[i]:
                total += (min(left[i],right[i]) - height[i])

        return total 
        