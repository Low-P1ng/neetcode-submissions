class Solution:
    def countSubstrings(self, s: str) -> int:

        res = [0]
        def check(s,l,r):
            if l>= 0 and r < len(s) and s[l] == s[r]:
                res[0]+=1
                check(s,l-1,r+1)
            return

        for i in range (len(s)):
            temp = check(s, i, i)
            temp2 = check(s,i , i+1)
        return res[0]