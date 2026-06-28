class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        temp = 0
        counter = 0
        while r < len(nums)-1:
            temp = r
            for i,n in enumerate(nums[l:r+1], start = l):
                if n+i > r:
                    r = n+i
                if r >= len(nums)-1:
                    break
            l = temp + 1
            counter += 1
        
        return counter