class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        return (new_nums[-1] * new_nums[-2]) - (new_nums[0] * new_nums[1])
