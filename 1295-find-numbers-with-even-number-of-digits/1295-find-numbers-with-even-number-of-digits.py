class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num = 0
        for i in nums:
            count = 0
            while True:
                if i<=0:
                    break
                i//=10
                count+=1
            if count%2==0:
                even_num+=1
        return even_num
            