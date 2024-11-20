class Solution:
    def isBalanced(self, num: str) -> bool:
        evenTotal = 0
        oddTotal = 0 
        for i in range(len(num)):
            if i%2==0:evenTotal+=int(num[i])
            else:oddTotal+=int(num[i])
        return evenTotal==oddTotal