class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum=nums[0]
        m_sum=nums[0]
        for n in nums[1:]:
            c_sum=max(n, c_sum + n)
            m_sum=max(c_sum, m_sum)
        return m_sum