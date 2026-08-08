class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int):
        total = 0
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                total+=self.matrix[i][j]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)