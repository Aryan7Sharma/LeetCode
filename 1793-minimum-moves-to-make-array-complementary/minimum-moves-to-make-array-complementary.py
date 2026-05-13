class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        l,r=0,len(nums)-1
        diff = {}
        while l<r:
            a = nums[l]
            b = nums[r]
            low = min(a,b)+1
            high = max(a,b)+limit
            s = a+b

            diff[2] = diff.get(2, 0)+2

            diff[low] = diff.get(low, 0)-1
            diff[high+1] = diff.get(high+1, 0)+1

            diff[s] = diff.get(s,0)-1
            diff[s+1] = diff.get(s+1, 0)+1

            l+=1
            r-=1

        ans = float('inf')
        curr = 0

        for target in range(2, 2*limit+1):
            curr+= diff.get(target,0)
            ans = min(curr, ans)
        return ans

        