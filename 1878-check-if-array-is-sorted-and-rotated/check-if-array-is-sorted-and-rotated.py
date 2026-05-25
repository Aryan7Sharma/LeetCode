class Solution:
    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        sorted_nums = sorted(nums)
        
        for i in range(size):
            lastele = nums.pop()
            print(lastele)
            nums = [lastele] + nums
            if nums == sorted_nums:return True
        return False