class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneakyNums = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:sneakyNums.append(nums[i])
        return sneakyNums

