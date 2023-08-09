class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum,digit_sum = 0,0
        for i in nums:
            element_sum+=i
            for j in str(i):
                digit_sum+=int(j)
        return abs(element_sum-digit_sum)
