class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c=0
        x=Counter(words1)
        y=Counter(words2)
        for i,j in x.items():
            if j == 1 and y[i] == 1:
                c+=1
        return c
