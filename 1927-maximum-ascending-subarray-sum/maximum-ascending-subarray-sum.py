class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximumSum = 0
        assSubArraySum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                maximumSum = max(maximumSum,assSubArraySum)
                assSubArraySum = nums[i]
            else:assSubArraySum+=nums[i]
        maximumSum = max(maximumSum,assSubArraySum)
        return maximumSum

