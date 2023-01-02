class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 1
        sub_num = s[0]
        for i in range(1, len(s)):
            if int(s[i])<=k:
                if int(sub_num+s[i])<=k:
                    print(sub_num, s[i])
                    sub_num+=s[i]
                    print(sub_num)
                else:
                    count+=1
                    sub_num=s[i]
            else:
                return -1
        return count
            