class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotationCount = len(nums)
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:l=m+1
            else:r=m
        if l!=0:rotationCount=l
        print(f"The original array was {nums} and it was rotated {rotationCount} times.")
        return nums[l]