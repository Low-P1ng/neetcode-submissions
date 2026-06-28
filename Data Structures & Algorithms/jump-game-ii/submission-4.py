class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        temp = 0
        counter = 0
        while r < len(nums)-1:
            temp = r
            for i in range(l, temp+1):
                if nums[i]+i > r:
                    r = nums[i]+i
                if r >= len(nums)-1:
                    break
            l = temp + 1
            counter += 1
        
        return counter