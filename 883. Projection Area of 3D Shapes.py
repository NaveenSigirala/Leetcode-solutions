class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(1 for row in grid for v in row if v)
        xz = sum(max(row) for row in grid)
        yz = sum(max(col) for col in zip(*grid))
        return xy + xz + yz
        
