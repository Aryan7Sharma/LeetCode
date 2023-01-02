class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
        return [dup, len(nums) if nums[len(nums) - 1] != len(nums) else missing]
        