class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=0
        for i in nums:
            if nums.count(i)%2==0:
                count += 1
        if count == len(nums):
            return True
        else:
            return False
