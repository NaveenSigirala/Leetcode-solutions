class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)[::-1]
        sum1,sum2=0,sum(nums)
        for i in range(len(nums)):
            sum1+=nums[i]
            sum2-=nums[i]
            if sum1>sum2:
                return nums[0:i+1]
