class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hash_set = set(nums)
        res = 0
        for num in nums:
            if num + diff in hash_set and num + 2*diff in hash_set:
                res += 1
        return res
