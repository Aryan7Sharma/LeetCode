class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatValue = 0
        length = len(nums)-1
        l,r=0,length
        while l<r:
            currConcat = str(nums[l]) + str(nums[r])
            concatValue+=int(currConcat)
            l+=1
            r-=1
        if length%2==0:concatValue+=nums[len(nums)//2]
        return concatValue
