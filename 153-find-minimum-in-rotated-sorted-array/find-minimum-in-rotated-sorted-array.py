class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotationCount = 1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                print(f"The original array was {nums} and it was rotated {rotationCount} times.")
                return nums[i]
            else:rotationCount+=1
        print(f"The original array was {nums} and it was rotated {rotationCount} times.")
        return nums[0]
        