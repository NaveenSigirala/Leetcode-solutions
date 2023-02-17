class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        c=0
        for x,y in zip(heights,h):
            if x!=y:
                c+=1
        return c
