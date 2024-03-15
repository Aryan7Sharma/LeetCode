class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsProd = 1
        flagZero = False
        countZero = 0
        for i in nums:
            if i == 0:
                flagZero = True
                countZero+=1
            else:
                numsProd*=i
            if countZero>1:
                nums = [0]*len(nums)
                return nums
        if flagZero:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i] = numsProd
                else: nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = numsProd//nums[i]
        return nums
        