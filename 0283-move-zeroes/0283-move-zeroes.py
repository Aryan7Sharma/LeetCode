class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans=[]
        for i in nums:
            if i!=0:ans.append(i)
        for i in range(len(nums)-len(ans)):
            ans.append(0)
        nums[:]=ans
        return nums
        
        