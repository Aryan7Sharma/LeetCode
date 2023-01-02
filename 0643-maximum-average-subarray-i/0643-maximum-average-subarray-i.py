class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        hashmap = {1:nums[0]}
        res = float('-inf') 
        for i in range(1, len(nums)):
            hashmap[i+1] = hashmap[i]+nums[i]
        print(hashmap ,len(hashmap))
        res = max(res, hashmap[k]/k)
        for i in range(k+1,len(hashmap)+1):
            res = max(res, (hashmap[i]-hashmap[i-k])/k)
        return res
        