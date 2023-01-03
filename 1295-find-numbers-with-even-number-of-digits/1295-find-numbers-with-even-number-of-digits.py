class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num = 0
        for i in nums:
            if len(str(i))%2 == 0:
                even_num+=1
        return even_num