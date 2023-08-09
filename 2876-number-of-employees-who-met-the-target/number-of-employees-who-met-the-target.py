class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        numofEmpComTarget = 0
        for i in hours:
            if i>=target:numofEmpComTarget+=1
            else:continue
        return numofEmpComTarget