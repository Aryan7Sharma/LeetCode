class Solution:
    def minElement(self, nums: List[int]) -> int:
        index = 0
        minimum = 100000
        for i in nums:
            numTotal = 0
            for num in str(i):
                numTotal+=int(num)
            nums[index] = numTotal
            index+=1
            minimum = min(minimum, numTotal)
        return minimum
        