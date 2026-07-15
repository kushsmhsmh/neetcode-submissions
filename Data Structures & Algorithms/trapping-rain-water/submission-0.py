class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        lmax, rmax, total = 0, 0, 0 
        while left < right:
            lmax = max(lmax, heights[left])
            rmax = max(rmax, heights[right])
            
            if lmax < rmax:
                total += lmax - heights[left]
                left += 1
            else:
                total += rmax - heights[right]
                right -= 1

        return total