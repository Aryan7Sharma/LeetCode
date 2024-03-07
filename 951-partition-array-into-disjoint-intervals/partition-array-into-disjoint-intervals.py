class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lmax = nums[0]
        rmax = -1
        pos = 1
        for i in range(1,len(nums)):
            if lmax>nums[i]:
                pos = i+1
                lmax = max(lmax,rmax)
                rax = -1
            elif rmax<nums[i]:
                rmax = nums[i]
        return pos

        