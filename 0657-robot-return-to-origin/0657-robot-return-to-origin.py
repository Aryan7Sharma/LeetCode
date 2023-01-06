class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l,r,u,d=0,0,0,0
        for i in moves:
            if i == "L":
                if r>0:
                    r-=1
                else:
                    l+=1
            elif i == "R":
                if l>0:
                    l-=1
                else:
                    r+=1
            elif i == "U":
                if d>0:
                    d-=1
                else:
                    u+=1
            elif i == "D":
                if u>0:
                    u-=1
                else:
                    d+=1
        return False if (l+r+u+d)>0 else True
            
        