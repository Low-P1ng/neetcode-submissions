class Solution:
    def reverse(self, x: int) -> int:
        neg = 2**31
        pos = 2**31 - 1
        rev = 0
        check = False

        if x < 0:
            check = True
        x = abs(x)

        while x >= 10:
            rev += x % 10
            rev *= 10
            x //= 10

        rev //= 10

        if check:
            if rev > neg // 10:
                return 0
            elif rev == neg // 10:
                if x > neg % 10:
                    return 0
            return -(rev * 10 + x)
        else:
            if rev > pos // 10:
                return 0
            elif rev == pos // 10:
                if x > pos % 10:
                    return 0
            return rev * 10 + x