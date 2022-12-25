class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def subsets(i=0, path=0):
            nonlocal res
            if i == len(nums):
                res += path
                return

            subsets(i + 1, path ^ nums[i])
            subsets(i + 1, path)

        subsets()
        return res
