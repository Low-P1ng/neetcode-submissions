class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        melem = nums[0]
        c = 1
        for elem in nums[1:]:
            if elem == melem:
                c+=1
                continue
            c-=1
            if c == 0:
                melem = elem
                c+=1
        return melem