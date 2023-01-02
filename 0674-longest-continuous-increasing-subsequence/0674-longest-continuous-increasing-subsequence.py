class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        subSeq = 1
        maxSeq_len = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                maxSeq_len = max(maxSeq_len, subSeq)
                subSeq = 1
            else:
                subSeq+=1
        maxSeq_len = max(maxSeq_len, subSeq)
        return maxSeq_len
            
        