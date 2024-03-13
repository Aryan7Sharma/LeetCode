class Solution:
    def pivotInteger(self, n: int) -> int:
        l,r=1,n
        lSum,rSum=1,n
        ans = -1
        while l<r:
            if lSum<rSum:
                l+=1
                lSum+=l
            else:
                r-=1
                rSum+=r
        if lSum==rSum:ans=l
        return ans
        