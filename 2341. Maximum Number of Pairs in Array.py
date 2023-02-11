class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0,0]
        for i in cnt.values():
            ans[0] += i//2
            ans[1] += i%2
        return ans
