class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while True:
            product = 0
            for elem in str(n):
                product += int(elem)*int(elem)
            if product == 1:
                return True
            if product in check:
                return False
            n = product
            check.add(product)
