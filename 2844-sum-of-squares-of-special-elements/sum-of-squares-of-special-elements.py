class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumofSquare = 0
        n = len(nums)
        for i in range(1,n+1):
	        if n%i==0:sumofSquare+=nums[i-1]**2
        return sumofSquare
