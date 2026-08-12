class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f=0
        s=0
        res = ''
        while f<len(word1) and s<len(word2):
            res+=word1[f]+word2[s]
            f+=1
            s+=1
        if f<len(word1):
            res+=word1[f:]
        if s<len(word2):
            res+=word2[s:]
        return res
        