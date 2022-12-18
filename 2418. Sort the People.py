class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [row[1] for row in sorted(zip(heights, names), reverse = True)]
