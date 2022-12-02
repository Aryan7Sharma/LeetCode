class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = [i for i in word1]
        temp = 1
        for j in word2:
                ans = ans[:temp]+[j]+ans[temp:]
                temp+=2
        return "".join(ans)