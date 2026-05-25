class Solution:
    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        if size<3:return True
        inversion_count = 0

        for i in range(1,size):
            if nums[i]<nums[i-1]:
                inversion_count+=1
                if inversion_count>1:return False
        if nums[0]<nums[size-1]:inversion_count+=1
        print(inversion_count)
        return inversion_count <= 1