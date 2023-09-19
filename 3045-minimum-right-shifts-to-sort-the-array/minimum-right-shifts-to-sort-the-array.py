class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        countRigthShift = 0
        i = 0
        while nums!=nums2 and i<len(nums):
          lastvalue = nums.pop()
          nums = [lastvalue] + nums
          i+=1
          countRigthShift+=1
        return -1 if nums!=nums2 else countRigthShift
