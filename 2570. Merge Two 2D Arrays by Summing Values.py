class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0 
        while i < len(nums1) or j < len(nums2): 
            if j == len(nums2) or i < len(nums1) and nums1[i][0] <= nums2[j][0]: 
                ans.append(nums1[i])
                i += 1
            else: 
                if ans and ans[-1][0] == nums2[j][0]: ans[-1][1] += nums2[j][1]
                else: ans.append(nums2[j])
                j += 1
        return ans
