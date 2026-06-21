class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(arr):
            arr = arr[:]
            if len(arr)<3:
                return max(arr)

            for i in range(len(arr)-3,-1,-1):
                arr[i] = arr[i] + max(arr[i+2:])  

            return max(arr)

        return max(solve(nums[1:]), solve(nums[:-1]))
            