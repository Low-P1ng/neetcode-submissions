class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L,R,M):
            left = nums[L:M+1]
            right = nums[M+1:R+1]
            i,j,k = L,0,0
            while j<len(left) and k<len(right):
                if left[j]<right[k]:
                    nums[i]=left[j]
                    j+=1
                else:
                    nums[i] = right[k]
                    k+=1
                i+=1

            while j<len(left):
                nums[i]=left[j]
                i+=1
                j+=1

            while k<len(right):
                nums[i]=right[k]
                i+=1
                k+=1

        def mergesort(l,r):
            if l>=r:
                return nums

            m = (l+r)//2
            mergesort(l,m)
            mergesort(m+1,r)
            merge(l,r,m)

            return nums

        return mergesort(0,len(nums)-1)