class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        bracket = []
        for i,e in enumerate(s):
            if e == ')':
                if bracket:
                    bracket.pop()
                    continue
                if star:
                    star.pop()
                    continue
                return False
            else:
                if e == '*':
                    star.append(i)
                else:
                    bracket.append(i)

        if len(star) < len(bracket):
            return False
        while bracket:
            if star[-1] > bracket[-1]:
                star.pop()
                bracket.pop()
            else:
                return False
        return True