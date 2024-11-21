class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = 100000
        for i in range(len(nums)):
            numTotal = 0
            for num in str(nums[i]):
                numTotal+=int(num)
            nums[i] = numTotal
            minimum = min(minimum, numTotal)
        return minimum
        