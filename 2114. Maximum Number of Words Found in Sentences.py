class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for i in sentences:
            count=i.split()
            
            l.append(len(count))
        return max(l)
