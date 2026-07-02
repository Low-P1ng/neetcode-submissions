class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        check = {'r':set(),'c':set()}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    check['r'].add(i)
                    check['c'].add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in check['r'] or j in check['c']:
                    matrix[i][j] = 0


        