class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxElement = max(nums)
        arrayLen = len(nums)
        if arrayLen!=maxElement+1:return False
        nums.sort()
        for i in range(1,maxElement+1):
            if nums[i-1]!=i:return False
        return True