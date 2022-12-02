class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = "" 
        flag=0
        temp=""
        for i in range(-1,-(len(s)+1),-1):
            if s[i] == '#':
                flag=2
            elif flag>0:
                if flag == 1:
                    temp+=s[i]
                    ans+=chr(int(temp[::-1])+96)
                    flag-=1
                    temp=""
                else:
                    temp+=s[i]
                    flag-=1
            else:
                ans+=chr(int(s[i])+96)
        return ans[::-1]
        