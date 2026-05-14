class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxNum = max(nums)
        numsLen=len(nums)
        if numsLen!=maxNum+1:return False
        nums.sort()
        for i in range(numsLen-1):
            if i+1!=nums[i]:return False
        return True
