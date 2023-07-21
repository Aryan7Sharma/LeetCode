class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        numofOperation = 0
        while num1!=0 and num2!=0:
            numofOperation+=1
            if num1>=num2:num1-=num2
            else:num2-=num1
        return numofOperation