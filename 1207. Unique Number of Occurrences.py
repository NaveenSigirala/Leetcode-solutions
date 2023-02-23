class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic=dict()
        s=set()
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic.values():
            s.add(i)
        return True if len(s)==len(dic) else False
