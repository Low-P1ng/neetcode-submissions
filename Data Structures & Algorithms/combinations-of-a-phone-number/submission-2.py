class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = dict(zip("23456789", ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]))
        res = []
        if not digits:
            return []
        def dfs(i,s):
            if i>= len(digits):
                res.append(s[:])
                return

            for letter in dic[digits[i]]:
                dfs(i+1,s+letter)

        dfs(0,'')
        return res