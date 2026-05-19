class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        numshash = {}
        for i in nums1:
            if i not in numshash:numshash[i]=1
        for i in nums2:
            if i in numshash:return i
        return -1