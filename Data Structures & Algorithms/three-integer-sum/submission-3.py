class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p = 0
        res = []
        while p < len(nums)-2:
            if p>0 and nums[p] == nums[p-1]:
                p+=1
                continue
            
            l = p+1
            r = len(nums)-1
            while l < r:
                if nums[p] + nums[l] + nums[r] == 0:
                    res.append([nums[p],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[p] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
            p+=1

        return res
