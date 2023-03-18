class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic={}
        l=97
        for i in distance:
            dic[chr(l)]=i
            l+=1
        for i in set(s):
            f=s.index(i)
            la=s.rindex(i)
            diff=la-f-1
            if dic[i]!=diff:
                return False
        return True 
               
