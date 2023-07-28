class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        flag = False
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    flag = True
                    break
            if not flag:ans+=1
            else:flag = False
        return ans