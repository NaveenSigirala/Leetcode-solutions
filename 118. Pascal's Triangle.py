class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(1,numRows + 1):
            row = [1] * i
            for j in range(1,i-1):
                row[j] = l[i-2][j] + l[i-2][j-1]
            l.append(row)
        return l
