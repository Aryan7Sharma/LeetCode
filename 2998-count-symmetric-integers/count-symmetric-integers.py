class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans= 0
        for i in range(low, high+1):
            s = str(i)
            t,n = 0,len(s)
            for j in range(n//2):
                t+= int(s[j]) - int(s[n-j-1]) 
            if n%2==0 and t==0:ans+=1
        return ans