#brute force solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = nums[0] + nums[1] + nums[2]
        numsLen = len(nums)
        nums.sort()
        for i in range(numsLen):
            left,right = i+1,numsLen-1
            while left<right:
                currSum = nums[i] + nums[left] + nums[right]
                if abs(target - currSum) < abs(target - closestSum):
                    closestSum = currSum
                if currSum == target:
                    return target
                if currSum<target:left+=1
                else:right-=1
        return closestSum

### got TLE in Brute Force solution.