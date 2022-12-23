class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        n = len(mat[0])
        for i in range(0, n):
            for j in range(0, n):
                if i==j:
                    sum1 += (mat[i][j])
                if ((i+j) == (n-1)):
                    sum2 += (mat[i][j])
                if i==j and ((i+j) == (n-1)):
                    sum3 += (mat[i][j])
        return sum1+sum2-sum3
