class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashmap = {i:1 for i in nums1}
        for i in nums2:
            if i in hashmap:return i
        return -1


