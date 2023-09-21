class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctElement = len(set(nums))
        count = 0
        print(distinctElement)
        for i in range(len(nums)):
            hashmap={}
            currdist = 0
            for j in range(i,len(nums)):
                if nums[j] in hashmap:hashmap[nums[j]]+=1
                else:
                    hashmap[nums[j]]=1
                    currdist+=1
                #subarray.append(nums[j])
                #print(subarray)
                if currdist == distinctElement:count+=1
        return count