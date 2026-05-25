class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        size = len(s)
        pre,f = [0]*size, [0]*size
        f[0] = 1
        for i in range(minJump):
            pre[i]=1
        for i in range(minJump, size):
            left,right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left<=0 else pre[left-1])
                f[i] = int(total!=0)
            pre[i] = pre[i-1] + f[i]
        return bool(f[size-1])
        