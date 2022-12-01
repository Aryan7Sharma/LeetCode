class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=[-1,1][x>0]
        result=0
        x=abs(x) 
        while x!=0:
            pops=x%10
            x/=10
            result=result*10+pops
        result=result*sign    
        if result>= -2**31 and result<= 2**31-1:
            return result 
        return 0
        