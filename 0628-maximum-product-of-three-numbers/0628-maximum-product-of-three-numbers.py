class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        min1,min2 = nums[:2]
        max1,max2,max3 = nums[-1:-4:-1]
        if min1>0 or min2>0:
            return max1*max2*max3
        return max(min1*min2*max1,max1*max2*max3)
            