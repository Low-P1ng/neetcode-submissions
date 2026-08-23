class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        p = 1
        pfinal = 0
        res = []
        while pfinal < len(nums)-3:
            if pfinal > 0 and nums[pfinal] == nums[pfinal - 1]:
                pfinal += 1
                p = pfinal + 1
                continue

            p = pfinal + 1
            while p < len(nums)-2:
                if p>pfinal+1 and nums[p] == nums[p-1]:
                    p+=1
                    continue
                
                l = p+1
                r = len(nums)-1
                while l < r:
                    total = nums[pfinal] + nums[p] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[pfinal],nums[p],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                    elif total > target:
                        r-=1
                    else:
                        l+=1
                p+=1
            pfinal +=1

        return res