class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1len,nums2len = len(nums1),len(nums2)
        numsDict = {}
        res = []
        if nums1len>nums2len:
            for i in nums1:
                if i not in numsDict:
                    numsDict[i]=1
            for i in set(nums2):
                if i in numsDict:
                    res.append(i)
        else:
            for i in nums2:
                if i not in numsDict:
                    numsDict[i]=1
            for i in set(nums1):
                if i in numsDict:
                    res.append(i)
        return res
        