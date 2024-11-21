class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = float('inf')
        for i in range(len(nums)):
            numTotal = 0
            for num in str(nums[i]):
                numTotal+=int(num)
            nums[i] = numTotal
            if(minimum>numTotal):minimum=numTotal
        return minimum
        