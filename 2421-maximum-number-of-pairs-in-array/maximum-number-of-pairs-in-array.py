class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        #first sort the nums
        if not nums:
            return []
        opera = 0
        leftInte = 0
        start = 0
        end = len(nums)
        output = []
        nums.sort()
        while start<end-1:
            if nums[start]==nums[start+1]:
                opera+=1
                start+=2
            else:
                leftInte+=1
                start+=1
        if(start<end):
            leftInte+=1
        output.append(opera)
        output.append(leftInte)
        return output


        