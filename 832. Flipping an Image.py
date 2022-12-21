class Solution:
    def flipAndInvertImage(self, A) -> List[List[int]]:
        return [[1 - x for x in A[i][::-1]] for i in range(len(A))]
