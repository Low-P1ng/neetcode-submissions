class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                most = max(most,heights[l]*(r-l))
                l+=1
            else:
                most = max(most,heights[r]*(r-l))
                r-=1
        return most