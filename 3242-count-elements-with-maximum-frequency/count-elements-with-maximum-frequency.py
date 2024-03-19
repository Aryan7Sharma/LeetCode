class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        totalmaxFreq = 0
        maxFreq = 1
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
                maxFreq = max(maxFreq, hashmap[i])
            else:
                hashmap[i]=1
        for v in hashmap.values():
            if v == maxFreq:totalmaxFreq+=maxFreq
        return totalmaxFreq