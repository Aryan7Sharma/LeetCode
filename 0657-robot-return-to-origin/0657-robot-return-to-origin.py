class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l,d=0,0
        for i in moves:
            if i == "L":
                l+=1
            elif i == "R":
                l-=1
            elif i == "U":
                d-=1
            elif i == "D":
                d+=1
        return l==0 and d==0
            
        