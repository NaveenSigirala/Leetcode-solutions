class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(1,len(nums),2):
            l.extend([nums[i]]*nums[i-1])
        return l 
