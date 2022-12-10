class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen_str=s[0]
        sub_string=""
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    sub_string = s[i:j+1]
                    if len(sub_string) > len(maxlen_str):
                        if sub_string == sub_string[::-1]:
                            maxlen_str = sub_string
        return maxlen_str
                    
        
            